# Statement for enabling the development environment
DEBUG = True

import os
#BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = 'somethingsecret'

SQLALCHEMY_DATABASE_URI = 'sqlite://'

# uncomment to use postgres and aws
#SQLALCHEMY_DATABASE_URI = 'postgres://{}:{}@{}/budgetreport'.format(os.environ['RDS_USER'], os.environ['RDS_PASSWRD'], os.environ['RDS_HOST'])

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'secret'
