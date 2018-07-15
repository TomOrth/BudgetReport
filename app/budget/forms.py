from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, IntegerField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo

class NewBudgetForm(FlaskForm):
    name     = TextField('Name', [
                Required(message='Name required')])
    amount   = IntegerField('Amount', [
                Required(message='Amount Required')])