"""
This module is the controller for user authentication
"""
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user

from app import db
from app.auth.form import AuthForm
from app.auth.models import User


auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Sign-up endpoint for users. Makes sure that a user with the same email does not exist
    :returns: A redirect to the home page if a user is already signed in, the main budget report page if the user successfully signs up, or the signup page if the user does input minimum requirements
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    signup_form = AuthForm(request.form)
    if request.method == 'POST' and signup_form.validate_on_submit():
        user_exists = User.query.filter_by(email=signup_form.email.data).scalar()
        # if user does not exist, we create a new one
        if user_exists is None:
            new_user = User(email=signup_form.email.data, password=signup_form.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('budget.report'))
        else:
            flash('User already exists')
            return redirect(url_for('auth.signup'))
    return render_template('auth/signup.html', form=signup_form, loggedin=current_user.is_authenticated, title='Sign-Up')

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    Sign-in route for users
    :returns: Redirect to the home page if there is a user signed in, the main budget page if the user successfully signs in now, or the sign-in page if they input the wrong credentials
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    signin_form = AuthForm(request.form)
    if request.method == 'POST' and signin_form.validate_on_submit():
        user_exists = User.query.filter_by(email=signin_form.email.data).scalar()
        # if the user does exit, we check the sign-in credentials
        if user_exists is not None:
            user = User.query.filter_by(email=signin_form.email.data).first()
            if user.check_password(signin_form.password.data):
                login_user(user)
                return redirect(url_for('budget.report'))
            else:
                flash('Incorrect Password')
                return redirect(url_for('auth.signin'))
        else:
            flash('No user with the specified email does not exist')
            return redirect(url_for('auth.signin'))
    return render_template('auth/signin.html', form=signin_form, loggedin=current_user.is_authenticated, title='Sign-In')

@auth.route('/logout')
@login_required
def logout():
    """
    Logs users out
    :returns: A redirect to the home page
    """
    logout_user()
    return redirect(url_for('home'))
