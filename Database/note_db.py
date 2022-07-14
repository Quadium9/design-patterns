from Database.model import NoteModel
from app import db


class Note(NoteModel):
    @staticmethod
    def update_note(note: NoteModel, note_id: int):
        try:
            note_db: NoteModel = db.session.query(NoteModel).filter(NoteModel.id == note_id).first()
            if note.title is not None:
                note_db.title = note.title
            if note.description is not None:
                note_db.description = note.description
            if note.planned_date is not None:
                note_db.planned_date = note.planned_date
            db.session.commit()
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
            return db.session.query(NoteModel).filter(NoteModel.planned_date == day, NoteModel.active == 1).all()
        except:
            return []

    @staticmethod
    def get_all_active():
        try:
            return db.session.query(NoteModel).filter(NoteModel.active == 1).all()
        except:
            return []

    @staticmethod
    def delete_note(note_id):
        try:
            note_db: NoteModel = db.session.query(NoteModel).get(note_id)
            note_db.active = 0
            db.session.commit()
            return True
        except:
            return False
