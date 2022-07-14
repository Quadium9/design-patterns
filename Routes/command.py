from __future__ import annotations
import datetime
from abc import ABC, abstractmethod
from Database.note_db import Note
from Database.model import NoteModel


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class UpdateNote(Command):
    def __init__(self, note_id, note):
        self.note_id = note_id
        self.note = note

    def execute(self):
        Note.update_note(note=self.note, note_id=self.note_id)


class DeleteNote(Command):
    def __init__(self, note_id):
        self.note_id = note_id

    def execute(self):
        Note.delete_note(self.note_id)


class TodayNote(Command):
    def __init__(self, user_id):
        self.user_id = user_id

    def execute(self):
        return Note.get_note_for_day(datetime.date.today(), self.user_id)


class AllActiveNote(Command):
    def __init__(self, user_id):
        self.user_id = user_id

    def execute(self):
        return Note.get_all_active(self.user_id)


class SaveNote(Command):
    def __init__(self, note):
        self.note = note

    def execute(self):
        return Note.add_note(self.note)


class Invoker:
    def delete_note(self, note_id):
        DeleteNote(note_id).execute()

    def update_note(self, note: NoteModel, note_id: int):
        UpdateNote(note_id, note).execute()

    def today_note(self, user_id):
        return TodayNote(user_id=user_id).execute()

    def save_note(self, note: NoteModel):
        SaveNote(note).execute()

    def get_all_active_note(self, user_id):
        return AllActiveNote(user_id=user_id).execute()
