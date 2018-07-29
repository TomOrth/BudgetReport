import json

from flask import Blueprint, request, current_app, redirect, url_for, jsonify
from flask_login import login_required, login_user, logout_user, current_user

from app import db
from app.expense.models import Expense
from app.budget.models import Budget

expense = Blueprint('expense', __name__, url_prefix='/expense')

@expense.route('/new', methods=['POST'])
def new():
    if request.method == 'POST':
        payload = request.json
        new_expense = Expense(budget_id=payload['budget_id'], user_id=current_user.id, description=payload['name'], amount=float(payload['amount']))
        budget = Budget.query.filter_by(id=payload['budget_id']).first()
        budget.amount -= new_expense.amount
        current_user.expenses.append(new_expense)
        db.session.add(current_user)
        db.session.add(new_expense)
        db.session.add(budget)
        db.session.commit()
        return jsonify(new_expense.as_dict()), 200
    return 'Unsupported request type', 405

@expense.route('/expenses')
def all():
    expense_map = {}
    for e in current_user.expenses:
        if e.budget_id in expense_map.keys():
            expense_map[e.budget_id].append(e.as_dict())
        else:
            expense_map[e.budget_id] = []
            expense_map[e.budget_id].append(e.as_dict())
    return jsonify(expense_map)