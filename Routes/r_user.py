from flask import Blueprint, redirect, url_for, flash, session
from Forms.login_forms import LoginForms, RegisterForms
from Database.user_db import User
from Database.creator import UserCreator

r_user = Blueprint('/user', __name__)


@r_user.post('/login')
def login():
    login_forms = LoginForms()
    if login_forms.is_submitted():
        created_user = UserCreator(password=login_forms.password.data,
                                   username=login_forms.username.data).factory_method()
        verified_user = User.login_user(created_user)
        if verified_user:
            session['user_id'] = verified_user.id
            session['username'] = verified_user.username
            return redirect(url_for('main'))
    return redirect(url_for('/'))


@r_user.get('/logout')
def logout():
    session.pop('user_id')
    session.pop('username')
    return redirect(url_for('start'))


@r_user.post('/register')
def register():
    register_form = RegisterForms()
    if register_form.is_submitted():
        if register_form.password.data == register_form.repeat_password.data:
            created_user = UserCreator(password=register_form.password.data,
                                       username=register_form.username.data).factory_method()
            save_user = User.add_user(created_user)
            if save_user:
                session['user_id'] = created_user.id
                session['username'] = created_user.username
                return redirect(url_for('main'))
        else:
            return flash('Incorrect repeated password.')
    return redirect(url_for('/'))
