from app import db
from app.base_model import Base
class Expense(Base):

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