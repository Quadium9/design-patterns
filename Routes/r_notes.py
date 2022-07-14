from Forms.note_forms import AddNoteForms, EditNoteForms, SearchNoteForms
from flask import Blueprint, render_template, flash, session, redirect, url_for
from Database.note_db import Note
from Database.creator import NoteCreator
from Routes.command import Invoker

r_note = Blueprint('/note', __name__)

invoker = Invoker()


@r_note.get('today_note_template')
def today_note_template():
    note_list = invoker.today_note()
    return render_template('today_note.html',
                           note_list=note_list)


@r_note.post('add_note')
def add_note():
    add_note_forms = AddNoteForms()
    new_note = NoteCreator(note_form=add_note_forms, user_id=session['user_id']).factory_method()
    invoker.save_note(note=new_note)
    flash('Add note')
    return redirect(url_for('start'))


@r_note.post('edit_note/<note_id>')
def edit_note(note_id):
    edit_note_forms = EditNoteForms()
    new_note = NoteCreator(note_form=edit_note_forms, user_id=session['user_id']).factory_method()
    invoker.update_note(note=new_note, note_id=note_id)
    flash('Edit note')
    return redirect(url_for('start'))


@r_note.get('search_note')
def search_note():
    search_note_forms = SearchNoteForms()
    return Note.search_note(search_note_forms.title.data,
                            search_note_forms.date_field.data)


@r_note.delete('delete_note/<note_id>')
def delete_note(note_id):
    invoker.delete_note(note_id=note_id)
    flash('Delete note')
    return redirect(url_for('start'))
