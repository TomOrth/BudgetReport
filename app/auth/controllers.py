from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user

from app import db
from app.auth.form import AuthForm
from app.auth.models import User


auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    signup_form = AuthForm(request.form)
    if request.method == 'POST' and signup_form.validate_on_submit():
        user_exists = User.query.filter_by(email=signup_form.email.data).scalar()
        if user_exists is None:
            new_user = User(email=signup_form.email.data, password=signup_form.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('home'))
        else:
            flash('User already exists')
            return redirect(url_for('auth.signin'))
    return render_template('auth/signup.html', form=signup_form, loggedin=current_user.is_authenticated)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    signin_form = AuthForm(request.form)
    if request.method == 'POST' and signin_form.validate_on_submit():
        user_exists = User.query.filter_by(email=signin_form.email.data).scalar()
        if user_exists is not None:
            user = User.query.filter_by(email=signin_form.email.data).first()
            if user.check_password(signin_form.password.data): 
                login_user(user)
            else:
                flash('Incorrect Password')
                return redirect(url_for('auth.signin'))
        else:
            flash('No user with the specified email does not exist')
            return redirect(url_for('auth.signin'))
    return render_template('auth/signin.html', form=signin_form, loggedin=current_user.is_authenticated)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))