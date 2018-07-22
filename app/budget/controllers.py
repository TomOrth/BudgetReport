import json

from flask import Blueprint, render_template, request, current_app, redirect, url_for, jsonify
from flask_login import login_required, login_user, logout_user, current_user

from app import db
from app.budget.models import Budget

budget = Blueprint('budget', __name__, url_prefix='/budget')

@budget.route('/report')
@login_required
def report():
    return render_template('budget/report.html', loggedin=current_user.is_authenticated)

@budget.route('/new', methods=['POST'])
def new():
    if request.method == 'POST':
        payload = request.json
        new_budget = Budget(user_id=current_user.id, name=payload['name'], amount=payload['amount'])
        current_user.budgets.append(new_budget)
        db.session.add(current_user)
        db.session.add(new_budget)
        db.session.commit()
        return 'Successful', 200
    return 'Unsupported request type', 405

@budget.route('/budgets')
def all():
    budgets = [b.as_dict() for b in current_user.budgets]
    return jsonify(budgets)
    

