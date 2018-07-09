from flask import Flask, render_template
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
from app.budget.models import Budget, Expense
from app.auth.models import User

app.register_blueprint(auth)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
    
@app.route("/")
def home():
    return render_template('index.html', loggedin=current_user.is_authenticated)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

db.create_all()

