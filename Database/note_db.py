from model import NoteModel
from app import db


class Note(NoteModel):
    def __init__(self, title, create_date, note, user_id):
        self.title = title
        self.create_date = create_date
        self.note = note
        self.user_id = user_id

    def add_note(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_note(self, note_id: int):
        try:
            note_db: NoteModel = db.session.query(NoteModel).get(note_id)
            if self.note:
                note_db.title = self.title
            if self.note:
                note_db.note = self.note
            if self.create_date:
                note_db.create_date = self.create_date
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
