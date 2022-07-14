from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Forms.note_forms import AddNoteForms, EditNoteForms, SearchNoteForms
from Forms.login_forms import LoginForms, RegisterForms

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Tajny z tajnych tokenow'
app.config['SQLALCHEMY_DATABASE_URI'] = "mariadb+mariadbconnector://root:root@localhost:3306/note"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from Routes.r_user import r_user
from Routes.r_notes import r_note
from Routes.command import Invoker
from Routes.decorator import check_user

app.register_blueprint(r_user, url_prefix='/user')
app.register_blueprint(r_note, url_prefix='/note')


@app.route('/start', methods=['GET', 'POST'])
@check_user
def main():
    add_note_forms = AddNoteForms()
    edit_note_forms = EditNoteForms()
    search_note_forms = SearchNoteForms()
    invoker = Invoker()
    note_list = invoker.get_all_active_note(session['user_id'])
    return render_template('main.html',
                           add_note_forms=add_note_forms,
                           edit_note_forms=edit_note_forms,
                           search_note_forms=search_note_forms,
                           note_list=note_list)


@app.route('/', methods=['GET', 'POST'])
def start():
    try:
        if session['user_id']:
            return redirect(url_for('main'))
    except:
        register_forms = RegisterForms()
        login_forms = LoginForms()
        return render_template('start.html',
                               register_forms=register_forms,
                               login_forms=login_forms)


if __name__ == '__main__':
    app.run()
