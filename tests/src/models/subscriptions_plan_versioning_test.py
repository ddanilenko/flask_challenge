from datetime import datetime

import pytest

from src.models.subscriptions_plan_versioning import SubscriptionPlanVersioning

invalid_cases = [
    {
        "subscription_id": 1111,
        "plan_id": 1,
        "start_eff_date": datetime(2020, 5, 12, 0, 0, 0),
        "end_eff_date": datetime(2020, 5, 29, 0, 0, 0)
    },
    {
        "subscription_id": 1111,
        "plan_id": 1,
        "start_eff_date": datetime(2020, 5, 14, 0, 0, 0),
        "end_eff_date": datetime(2020, 5, 29, 0, 0, 0)
    },
    {
        "subscription_id": 1111,
        "plan_id": 1,
        "start_eff_date": datetime(2020, 5, 12, 0, 0, 0),
        "end_eff_date": datetime(2020, 5, 27, 0, 0, 0)
    }
]


@pytest.mark.parametrize("kwargs", invalid_cases)
def test_model_dates_validation(kwargs, app):
    with pytest.raises(AssertionError):
        SubscriptionPlanVersioning(**kwargs)
