from flask import Blueprint
from Forms.login_forms import LoginForms, RegisterForms
from Database.user_db import User

r_user = Blueprint('/user', __name__)


@r_user.post('/login')
def login():
    login_forms = LoginForms()

    pass


@r_user.post('/register')
def register():
    pass
