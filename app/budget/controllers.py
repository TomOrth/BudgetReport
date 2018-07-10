from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

budget = Blueprint('budget', __name__, url_prefix='/budget')

@budget.route('/report')
@login_required
def report():
    return render_template('budget/report.html', loggedin=current_user.is_authenticated)

