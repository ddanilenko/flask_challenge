import pytest

from src.models.subscriptions_plan_versioning import SubscriptionPlanVersioning
from src.tasks.plans import get_last_subscription_plan, query_subscription_plans


@pytest.mark.parametrize("kwargs, expected_len", [
    ({}, 4),
    ({"id": 1}, 1),
    ({"plan_id": 1}, 3)
])
def test_get_last_subscription_plan(kwargs, expected_len, app):
    versions = SubscriptionPlanVersioning.query.filter_by(**kwargs).all()
    result = len(get_last_subscription_plan(versions))
    assert result == expected_len


@pytest.mark.parametrize("billing_cycle_id, subscription_id, expected", [
    (1, None, {1: [1], 2: [3]}),
    (2, None, {1: [2, 4]}),
    (3, None, {1: [4]}),
    (1, 1, {1: [1]}),
    (1, 2, {}),
])
def test_query_subscription_plans(billing_cycle_id, subscription_id, expected, app):
    result = query_subscription_plans(billing_cycle_id, subscription_id=subscription_id)
    assert result == expected


def test_query_subscription_plans_with_wrong_billing_cycle(billing_cycle_id=999):
    with pytest.raises(Exception):
        query_subscription_plans(billing_cycle_id)
