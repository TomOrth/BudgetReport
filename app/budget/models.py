"""
This module contains models related to the budgets
"""
from app.base_model import Base
from app import db

class Budget(Base):
    """
    Class that represents the Budget for a user
    current schema (particular to this model):
        user_id: int,
        name: string,
        amount: float,
        initial_amount: float
        expenses: database relationship
    :param user_id: id of the user that made this budget
    :param name: Name of the budget
    :param amount: Amount remaining in the budget
    :param initial_amount: Initial amount for the budget
    :type user_id: int
    :type name: str
    :type amount: float
    :type initial_amount: float
    """
    __tablename__ = 'budget'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    name = db.Column(db.String(128), nullable=False)

    amount = db.Column(db.Float)

    intial_amount = db.Column(db.Float)

    expenses = db.relationship('Expense')

    def __init__(self, user_id, name, amount, intial_amount):
        self.user_id = user_id
        self.name = name
        self.amount = amount
        self.intial_amount = intial_amount
