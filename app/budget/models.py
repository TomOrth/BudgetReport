from app.base_model import Base
from app import db

class Budget(Base):

    __tablename__ = 'budget'
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    name = db.Column(db.String(128), nullable=False)

    expenses = db.relationship('Expense', back_populates='expense')

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Expense(Base):

    __tablename__ = 'expense'

    description = db.Column(db.String(128), nullable=False)

    amount = db.Column(db.Integer)

    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'))

    def __init__(self, description, amount, budget_id):
        self.description = description
        self.amount = amount
        self.budget_id = budget_id