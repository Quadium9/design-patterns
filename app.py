from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from Forms.note_forms import AddNoteForms, EditNoteForms, SearchNoteForms
from Forms.login_forms import LoginForms, RegisterForms

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Tajny z tajnych tokenow'
app.config['SQLALCHEMY_DATABASE_URI'] = "mariadb+mariadbconnector://root:root@localhost:3306/note"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/start')
def main():
    add_note_forms = AddNoteForms()
    edit_note_forms = EditNoteForms()
    search_note_forms = SearchNoteForms()
    return render_template('main.html',
                           add_note_forms=add_note_forms,
                           edit_note_forms=edit_note_forms,
                           search_note_forms=search_note_forms)


@app.route('/')
def start():
    register_forms = RegisterForms()
    login_forms = LoginForms()
    return render_template('start.html',
                           register_forms=register_forms,
                           login_forms=login_forms)


if __name__ == '__main__':
    app.run()
