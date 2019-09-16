"""
This module contains models related to users and user authentication
"""
from app.base_model import Base
from app.extensions import bcrypt
from app import db

from flask_login import UserMixin

class User(Base, UserMixin):
    """
    User model that represents the user of the application
    Current schema (specific to this model):
        email: str,
        password: hashed,
        budgets: entries in the budget table,
        expenses: entries in the expense table
    :param email: User's email
    :param password: User's password
    :type email: str
    :type password: str
    """
    __tablename__ = 'user'

    # Identification Data: email & password
    email    = db.Column(db.String(128),  nullable=False,
                                            unique=True)
    password = db.Column(db.Binary(128), nullable=False)

    budgets = db.relationship('Budget')

    expenses = db.relationship('Expense')

    # New instance instantiation procedure
    def __init__(self, email, password):

        self.email    = email
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """
        Set's a user's password to a hashed version of their desired password
        :param password: User's password
        :type password: str
        """
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Verify password against stored hashed password.

        :param str value: The password to verify.
        :return: True if the password matches the stored hashed password.
        :rtype: bool
        """
        return bcrypt.check_password_hash(self.password, value)

    def __repr__(self):
        """
        Creates a string representation of the User
        :return: User string representation
        :rtype: str
        """
        return '<User %r>' % (self.email)
