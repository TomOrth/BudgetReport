"""
This module contains the controller for the budgets of the application
"""
import json

from flask import Blueprint, render_template, request, current_app, redirect, url_for, jsonify
from flask_login import login_required, login_user, logout_user, current_user

from app import db
from app.budget.models import Budget

budget = Blueprint('budget', __name__, url_prefix='/budget')

@budget.route('/report')
@login_required
def report():
    """
    Route that renders the budget report page page
    :returns: A redirect to the budget report page
    """
    return render_template('budget/report.html', loggedin=current_user.is_authenticated, title='Report')

@budget.route('/new', methods=['POST'])
def new():
    """
    Route to create a new budget
    :returns: Status message to indicate if the creation was sucessful
    :rtype: str, int
    """
    if request.method == 'POST':
        payload = request.json
        budget_exists = Budget.query.filter_by(name=payload['name']).scalar()
        if budget_exists is None:
            new_budget = Budget(user_id=current_user.id, name=payload['name'], amount=float(payload['amount']), intial_amount=float(payload['amount']))
            current_user.budgets.append(new_budget)
            db.session.add(current_user)
            db.session.add(new_budget)
            db.session.commit()
            return jsonify(new_budget.as_dict()), 200
        return 'Budget already exists', 500
    return 'Unsupported request type', 405

@budget.route('/all')
def all():
    """
    Route to get all budgets as json
    :returns: JSON of all the budgets
    :rtype: str
    """
    budgets = [b.as_dict() for b in current_user.budgets]
    return jsonify(budgets)

@budget.route('/delete', methods=['POST'])
def delete():
    """
    Route that delets a specific budget from the database
    :returns: Message with status and status code
    :rtype: str, int
    """
    if request.method == 'POST':
        payload = request.json
        budget = Budget.query.filter_by(name=payload['name']).first()
        budget_id = budget.id
        for e in budget.expenses:
            db.session.delete(e)
        db.session.delete(budget)
        db.session.commit()
        return jsonify(budget_id), 200
    return 'Unsupported request type', 405

