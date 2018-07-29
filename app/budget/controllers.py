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
        budget_exists = Budget.query.filter_by(name=payload['name']).scalar()
        if budget_exists is None:
            new_budget = Budget(user_id=current_user.id, name=payload['name'], amount=float(payload['amount']))
            current_user.budgets.append(new_budget)
            db.session.add(current_user)
            db.session.add(new_budget)
            db.session.commit()
            current_app.logger.info(new_budget.id)
            return jsonify(new_budget.as_dict()), 200
        return 'Budget already exists', 500
    return 'Unsupported request type', 405

@budget.route('/budgets')
def all():
    budgets = [b.as_dict() for b in current_user.budgets]
    return jsonify(budgets)
    

