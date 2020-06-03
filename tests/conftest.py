import pytest

from config import TestConfig
from src import create_app
from src.models.cycles import BillingCycle
from src.models.subscriptions import Subscription
from src.models.subscriptions_plan_versioning import SubscriptionPlanVersioning
from tests.db_test_data import subscription_data_list, versions_data_list, billing_cycle_data_list


def init_db(db):
    for subscription_data in subscription_data_list:
        db.session.add(Subscription(**subscription_data))
    db.session.commit()
    for version_data in versions_data_list:
        db.session.add(SubscriptionPlanVersioning(**version_data))
    db.session.commit()
    for billing_cycle_data in billing_cycle_data_list:
        db.session.add(BillingCycle(**billing_cycle_data))
    db.session.commit()


# TODO: Figure out why scope=session causes failures for test_query_subscription_plans
@pytest.fixture()
def app():
    app = create_app(TestConfig)
    db = app.extensions["sqlalchemy"].db
    with app.app_context():
        db.create_all()
        init_db(db)
        yield app
        db.session.remove()
        db.drop_all()
