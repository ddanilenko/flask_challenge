"""Plan related tasks"""
from celery.utils.log import get_task_logger
from flask import current_app
from sqlalchemy import or_, not_

from att import celery
from src.models.cycles import BillingCycle
from src.models.subscriptions_plan_versioning import SubscriptionPlanVersioning

log = get_task_logger(__name__)


def get_last_subscription_plan(versions):
    """Filter latest subscriptions plan version for each subscription
    :param versions: List of SubscriptionPlanVersioning for a billing cycle
    :return: List of latest SubscriptionPlanVersioning
    """
    result = {}
    for version in versions:
        if version.subscription_id not in result or result[version.subscription_id].create_date <= version.create_date:
            result[version.subscription_id] = version
    return list(result.values())


@celery.task()
def query_subscription_plans(billing_cycle_id, subscription_id=None):
    """ Get plans and its subscribtions
    :param billing_cycle_id: int billing cycle id for filter
    :param subscription_id: int subscription id for filter(optional)
    :return: dict plan key with List of SubscriptionPlanVersioning as a value
    """

    plan_subscription_versions = []
    additional_kwargs = {"subscription_id": subscription_id} if subscription_id else {}
    db = current_app.extensions['migrate'].db

    billing_cycle = BillingCycle.query.filter_by(id=billing_cycle_id).one()
    if not billing_cycle:
        log.debug(f"There is no billing cycle with id: {billing_cycle_id}")
        raise Exception(f"There is no billing cycle with id: {billing_cycle_id}")

    versions = db.session.query(SubscriptionPlanVersioning).filter(
        not_(or_(SubscriptionPlanVersioning.start_eff_date >= billing_cycle.end_date,
                 SubscriptionPlanVersioning.end_eff_date <= billing_cycle.start_date))
    ).filter_by(**additional_kwargs).all()
    if versions:
        plan_subscription_versions = get_last_subscription_plan(versions)

    plans = {}
    for version in plan_subscription_versions:
        if version.plan_id not in plans:
            plans[version.plan_id] = []
        plans[version.plan_id].append(version.subscription_id)

    return plans
