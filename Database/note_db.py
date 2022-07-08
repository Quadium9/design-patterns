from model import NoteModel
from app import db


class Note(NoteModel):
    @staticmethod
    def update_note(note: NoteModel, note_id: int):
        try:
            note_db: NoteModel = db.session.query(NoteModel).get(note_id)
            if note.note:
                note_db.title = note.title
            if note.note:
                note_db.note = note.note
            if note.create_date:
                note_db.create_date = note.create_date
            return True
        except:
            return False

    @staticmethod
    def add_note(note: NoteModel):
        try:
            db.session.add(note)
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def get_note_for_day(day):
        try:
            return db.session.query(NoteModel).filter(NoteModel.create_date == day).all()
        except:
            return []

    @staticmethod
    def get_note_for_user(user_id):
        try:
            return db.session.query(NoteModel).filter(NoteModel.user_id == user_id).all()
        except:
            return []

    @staticmethod
    def search_note(title: str, planned_date):
        try:
            result = db.session.query(NoteModel)
            if title:
                result += result.filter(NoteModel.title == title)
            if planned_date:
                result += result.filter(NoteModel.planned_date == title)
            return result.all()
        except:
            return []

    @staticmethod
    def delete_note(note_id):
        try:
            db.session.query().filter(NoteModel.id == note_id).delete()
            return True
        except:
            return False
