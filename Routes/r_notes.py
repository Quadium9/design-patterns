from Forms.note_forms import AddNoteForms, EditNoteForms, SearchNoteForms
from flask import Blueprint, render_template, session, redirect, url_for
from Database.note_db import Note
from Database.creator import NoteCreator
from Routes.command import Invoker
from Routes.decorator import check_user

r_note = Blueprint('/note', __name__)
invoker = Invoker()


@r_note.get('today_note_template')
@check_user
def today_note_template():
    add_note_forms = AddNoteForms()
    edit_note_forms = EditNoteForms()
    search_note_forms = SearchNoteForms()
    note_list = invoker.today_note()
    return render_template('today_note.html',
                           add_note_forms=add_note_forms,
                           edit_note_forms=edit_note_forms,
                           search_note_forms=search_note_forms,
                           note_list=note_list)


@r_note.post('add_note')
@check_user
def add_note():
    add_note_forms = AddNoteForms()
    new_note = NoteCreator(note_form=add_note_forms, user_id=session['user_id']).factory_method()
    invoker.save_note(note=new_note)
    return redirect(url_for('start'))


@r_note.post('edit_note/<note_id>')
@check_user
def edit_note(note_id):
    edit_note_forms = EditNoteForms()
    new_note = NoteCreator(note_form=edit_note_forms, user_id=session['user_id']).factory_method()
    invoker.update_note(note=new_note, note_id=note_id)
    return redirect(url_for('start'))


@r_note.get('search_note')
@check_user
def search_note():
    search_note_forms = SearchNoteForms()
    return Note.search_note(search_note_forms.title.data,
                            search_note_forms.date_field.data)


@r_note.post('delete_note/<note_id>')
@check_user
def delete_note(note_id):
    invoker.delete_note(note_id=note_id)
    return redirect(url_for('start'))
