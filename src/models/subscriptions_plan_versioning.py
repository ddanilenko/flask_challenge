"""Subscription Plan Versioning related models and database functionality"""
from datetime import datetime

from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates

from src.models.base import db
from src.models.subscriptions import Subscription


class SubscriptionPlanVersioning(db.Model):
    """Model class to represent versioning for subscriptions-plans"""

    __tablename__ = "subscription_plan_versioning"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_eff_date = db.Column(db.TIMESTAMP(timezone=True))
    end_eff_date = db.Column(db.TIMESTAMP(timezone=True))
    create_date = db.Column(db.TIMESTAMP(timezone=True), default=datetime.utcnow())

    subscription_id = db.Column(db.Integer, db.ForeignKey('subscriptions.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('plans.id'), nullable=False)
    subscription = db.relationship("Subscription", foreign_keys=[subscription_id], lazy="select")
    plan = db.relationship("Plan", foreign_keys=[plan_id], lazy="select")

    __table_args__ = (
        CheckConstraint('start_eff_date <= end_eff_date'),
    )

    def __repr__(self):  # pragma: no cover
        return (
            f"<{self.__class__.__name__}: {self.id}, "
            f"start_eff_date: {self.start_eff_date}, end_eff_date: {self.end_eff_date}>, "
            f"<subscription: {self.subscription_id}>, "
            f"<plan: {self.plan_id}>"
        )

    @validates("start_eff_date", "end_eff_date", "subscription_id")
    def validate_dates(self, key, field):
        """
        Validates start_eff_date to be greater than activation date in correspond subscription
        Validates end_eff_date to be less than expiry date in correspond subscription
        Handle different order of keys in SubscriptionPlanVersioning creation
        """

        if key == "subscription_id":
            subscr = Subscription.query.filter_by(id=field).one()
            if isinstance(self.start_eff_date,
                          datetime) and subscr.activation_date and self.start_eff_date < subscr.activation_date:
                raise AssertionError(
                    "The start effective date of plan must be greater-or-equal than the subscription activation date")
            if isinstance(self.end_eff_date,
                          datetime) and subscr.expiry_date and self.end_eff_date > subscr.expiry_date:
                raise AssertionError(
                    "The end effective date of plan must be less-or-equal than the subscription expiry date")

        if key == 'start_eff_date' and self.subscription_id:
            subscr = Subscription.query.filter_by(id=self.subscription_id).one()
            if subscr.activation_date and field < subscr.activation_date:
                raise AssertionError(
                    "The start effective date of plan must be greater-or-equal than the subscription activation date")
        if key == 'end_eff_date' and self.subscription_id:
            subscr = Subscription.query.filter_by(id=self.subscription_id).one()
            if subscr.expiry_date and field > subscr.expiry_date:
                raise AssertionError(
                    "The end effective date of plan must be less-or-equal than the subscription expiry date")
        return field

    # @property
    # def start_eff_date(self):
    #     return self._start_eff_date
    #
    # @start_eff_date.setter
    # def start_eff_date(self, start_eff_date):
    #     """
    #     Can be use for dates correction, but I prefer to use validation and app-level correction
    #     """
    #     if self.subscription_id:
    #         subscr = Subscription.query.filter_by(id=self.subscription_id).one()
    #         start_eff_date = max(start_eff_date, subscr.activation_date)
    #     self._start_eff_date = start_eff_date
