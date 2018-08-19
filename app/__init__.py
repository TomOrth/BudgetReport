from flask import Flask, render_template, redirect, url_for
from flask_login import current_user, LoginManager
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
login_manager = LoginManager()

# Configurations
app.config.from_object('config')
login_manager.init_app(app)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app.auth.controllers import auth
from app.budget.controllers import budget
from app.expense.controllers import expense
from app.budget.models import Budget
from app.expense.models import Expense
from app.auth.models import User

app.register_blueprint(auth)
app.register_blueprint(budget)
app.register_blueprint(expense)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
    
@app.route("/")
def home():
    if current_user.is_authenticated: 
        return redirect(url_for('budget.report'))
    return render_template('index.html', loggedin=current_user.is_authenticated, title='Home')

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('auth.signup'))

db.create_all()

