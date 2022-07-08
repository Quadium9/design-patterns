from __future__ import annotations
from abc import ABC, abstractmethod
from Database.note_db import Note
from Database.model import NoteModel


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class UpdateNote(Command):
    def __init__(self, note_id, note: NoteModel):
        self.note_id = note_id
        self.note = note

    def execute(self) -> None:
        Note.update_note(self.note_id, self.note)


class DeleteNote(Command):
    def __init__(self, note_id):
        self.note_id = note_id

    def execute(self) -> None:
        Note.delete_note(self.note_id)


class Invoker:
    def delete_note(self, note_id):
        DeleteNote(note_id).execute()

    def update_note(self, note_id: int, note: NoteModel):
        UpdateNote(note_id, note).execute()
