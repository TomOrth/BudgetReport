"""
This module contains models related to expenses
"""

from app import db
from app.base_model import Base
class Expense(Base):
    """
    Model representing a user expense
    current schema (particular to this model):
        description: str,
        amount: int,
        budget_id: int,
        user_id: int
    :param description: Description of the expense
    :param amount: Amount the expense costed
    :param budget_id: Budget id for the budget this expense related to
    :param user_id: User id that this expense was made for
    :type description: String
    :type amount: int
    :type budget_id: int
    :type user_id: int
    """
    __tablename__ = 'expense'

    description = db.Column(db.String(128), nullable=False)

    amount = db.Column(db.Float)

    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, description, amount, budget_id, user_id):
        self.description = description
        self.amount = amount
        self.budget_id = budget_id
        self.user_id = user_id
