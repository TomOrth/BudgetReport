"""
This module contains the controller for the expense logic
"""
import json

from flask import Blueprint, request, current_app, redirect, url_for, jsonify
from flask_login import login_required, login_user, logout_user, current_user

from app import db
from app.expense.models import Expense
from app.budget.models import Budget

expense = Blueprint('expense', __name__, url_prefix='/expense')

@expense.route('/new', methods=['POST'])
def new():
    """
    Route that creates a new Expense
    :returns: message and status code
    :rtype: str, int
    """
    if request.method == 'POST':
        payload = request.json
        expense = None
        new_expense = Expense(budget_id=payload['budget_id'], user_id=current_user.id, description=payload['name'], amount=float(payload['amount']))
        existing_expense = Expense.query.filter_by(description=new_expense.description, budget_id=new_expense.budget_id).scalar()
        budget = Budget.query.filter_by(id=payload['budget_id']).first()
        if budget.amount < new_expense.amount:
            return 'Cannot add expense, your budget will go to 0!', 500
        budget.amount -= new_expense.amount
        if existing_expense is None:
            current_user.expenses.append(new_expense)
            expense = new_expense
        else:
            old_expense = Expense.query.filter_by(description=new_expense.description, budget_id=new_expense.budget_id).first()
            old_expense.amount += new_expense.amount
            expense = old_expense
        db.session.add(current_user)
        db.session.add(expense)
        db.session.add(budget)
        db.session.commit()
        return jsonify(new_expense.as_dict()), 200
    return 'Unsupported request type', 405

@expense.route('/all')
def all():
    """
    Route to retrieve all the expenses
    :returns: message and status code
    :rtype: str, int
    """
    expense_map = {}
    for e in current_user.expenses:
        if e.budget_id in expense_map.keys():
            expense_map[e.budget_id].append(e.as_dict())
        else:
            expense_map[e.budget_id] = []
            expense_map[e.budget_id].append(e.as_dict())
    return jsonify(expense_map)

@expense.route('/delete', methods=['POST'])
def delete():
    """
    Route to delete an expense
    :returns: message and status code
    :rtype: str, int
    """
    if request.method == 'POST':
        payload = request.json
        expense = Expense.query.filter_by(description=payload['name']).first()
        budget = Budget.query.filter_by(id=expense.budget_id).first()
        budget_id = expense.budget_id
        budget.amount += expense.amount
        db.session.delete(expense)
        db.session.commit()
        return jsonify(budget_id), 200
    return 'Unsupported request type', 405
