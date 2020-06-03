from datetime import datetime

subscription_data_list = [
    {
        "id": 1111,
        "phone_number": 1111,
        "activation_date": datetime(2020, 5, 13, 0, 0, 0),
        "expiry_date": datetime(2020, 5, 28, 0, 0, 0),
        "plan_id": 1,
    },
    {
        'id': 1,
        'phone_number': '1111111111',
        'status': 'active',
        'plan_id': 3
    },
    {
        'id': 2,
        'phone_number': '2222222222',
        'status': 'suspended',
        'plan_id': 1
    },
    {
        'id': 3,
        'phone_number': '3333333333',
        'status': 'new',
        'plan_id': 2
    },
    {
        'id': 4,
        'phone_number': '4444444444',
        'status': 'expired',
        'plan_id': 2
    }
]

versions_data_list = [
    {
        "start_eff_date": datetime(2019, 8, 1),
        "end_eff_date": datetime(2019, 9, 1),
        "create_date": datetime(2019, 8, 1),
        "subscription_id": 1,
        "plan_id": 2},
    {
        "start_eff_date": datetime(2019, 8, 1),
        "end_eff_date": datetime(2019, 9, 1),
        "create_date": datetime(2019, 8, 12),
        "subscription_id": 1,
        "plan_id": 1},
    {
        "start_eff_date": datetime(2019, 9, 1),
        "end_eff_date": datetime(2019, 10, 1),
        "create_date": datetime(2019, 9, 1),
        "subscription_id": 2,
        "plan_id": 3},
    {
        "start_eff_date": datetime(2019, 9, 1),
        "end_eff_date": datetime(2019, 10, 1),
        "create_date": datetime(2019, 9, 12),
        "subscription_id": 2,
        "plan_id": 1},
    {
        "start_eff_date": datetime(2019, 8, 13),
        "end_eff_date": datetime(2019, 9, 1),
        "create_date": datetime(2019, 8, 1),
        "subscription_id": 3,
        "plan_id": 2},
    {
        "start_eff_date": datetime(2019, 9, 1),
        "end_eff_date": datetime(2019, 9, 18),
        "create_date": datetime(2019, 9, 1),
        "subscription_id": 4,
        "plan_id": 1},
    {
        "start_eff_date": datetime(2019, 10, 1),
        "end_eff_date": datetime(2019, 11, 1),
        "create_date": datetime(2019, 10, 1),
        "subscription_id": 4,
        "plan_id": 1}
]

billing_cycle_data_list = [
    {
        'id': 1,
        'start_date': datetime(2019, 8, 1),
        'end_date': datetime(2019, 9, 1),
    },
    {
        'id': 2,
        'start_date': datetime(2019, 9, 1),
        'end_date': datetime(2019, 10, 1),
    },
    {
        'id': 3,
        'start_date': datetime(2019, 10, 1),
        'end_date': datetime(2019, 11, 1),
    }
]
