from functools import wraps
from flask import session, render_template
from Forms.login_forms import RegisterForms, LoginForms


def check_user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            if not session['user_id'] and not session['username']:
                session.pop('user_id')
                session.pop('username')
                register_forms = RegisterForms()
                login_forms = LoginForms()
                return render_template('start.html',
                                       register_forms=register_forms,
                                       login_forms=login_forms)
        except:
            register_forms = RegisterForms()
            login_forms = LoginForms()
            return render_template('start.html',
                                   register_forms=register_forms,
                                   login_forms=login_forms)

        return f(*args, **kwargs)
    return decorated
