import json

from flask import Blueprint, request, current_app, redirect, url_for, jsonify
from flask_login import login_required, login_user, logout_user, current_user

from app import db
from app.expense.models import Expense

expense = Blueprint('expense', __name__, url_prefix='/expense')

@expense.route('/new', methods=['POST'])
def new():
    if request.method == 'POST':
        payload = request.json
        new_expense = Expense(budget_id=payload['budget_id'], user_id=current_user.id, description=payload['name'], amount=payload['amount'])
        current_user.expenses.append(new_expense)
        db.session.add(current_user)
        db.session.add(new_expense)
        db.session.commit()
        return 'Successful', 200
    return 'Unsupported request type', 405

@expense.route('/expenses')
def all():
    expenses = [e.as_dict() for e in current_user.expenses]
    return jsonify(expenses)