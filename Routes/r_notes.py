import datetime
from Forms.note_forms import AddNoteForms, EditNoteForms, SearchNoteForms
from flask import Blueprint, render_template, flash
from Database.note_db import Note

r_note = Blueprint('/note', __name__)


@r_note.route('/search_note_template')
def search_note_template():
    search_note_forms = SearchNoteForms()
    return render_template('search_note.html',
                           search_note_forms=search_note_forms)


@r_note.get('/today_note_template')
def today_note_template():
    return render_template('today_note.html',
                           note_list=Note.get_note_for_day(datetime.date.today()))


@r_note.post('/add_note')
def add_note():
    add_note_forms = AddNoteForms()
    if Note(title=add_note_forms.title.data,
            note=add_note_forms.description.data,
            user_id='',
            active=1,
            create_date=add_note_forms.date_field.data).add_note():
        return flash('Add note')
    return flash("Didn't add note")


@r_note.post('/edit_note')
def edit_note():
    edit_note_forms = EditNoteForms()
    if Note(title=edit_note_forms.title.data,
            note=edit_note_forms.description.data,
            user_id='',
            create_date=edit_note_forms.date_field.data):
        return flash('Edit note')
    return flash("Didn't edit note")


@r_note.get('/search_note')
def search_note():
    search_note_forms = SearchNoteForms()
    return Note.search_note(search_note_forms.title.data,
                            search_note_forms.date_field.data)
