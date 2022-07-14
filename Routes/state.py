from __future__ import annotations
from abc import ABC, abstractmethod
from flask import session
from Database.note_db import Note
from Database.model import NoteModel


class Context:
    _state = None
    _note = None
    _user = None

    def __init__(self, state: State, note, user):
        self.transition_to(state, note, user)

    def transition_to(self, state: State, note, user):
        self._state = state
        self._note = note
        self._user = user
        self._state.context = self

    def update(self, note, note_id):
        self._state.update(note, note_id)

    def delete(self, note):
        self._state.delete(note)

    def read(self, note):
        self._state.read(note)


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context):
        self._context = context

    @abstractmethod
    def create(self, note, user):
        pass

    @abstractmethod
    def update(self, note, note_id):
        pass

    @abstractmethod
    def delete(self, note):
        pass

    @abstractmethod
    def read(self, note):
        pass


class UpdateNote(State):
    def update(self, note, note_id):
        pass

    def delete(self, note):
        pass

    def read(self, note):
        self.context.transition_to(ReadNote(), note, session['user_id'])

    def create(self, note, user):
        pass


class ReadNote(State):
    def update(self, note, note_id):
        self.context.transition_to(UpdateNote(), note, session['user_id'])
        Note.update_note(note, note_id)

    def delete(self, note: int):
        self.context.transition_to(DeleteNote(), note, session['user_id'])
        Note.delete_note(note)

    def read(self, note):
        pass

    def create(self, note: NoteModel, user):
        self.context.transition_to(CreateNote(), note, session['user_id'])
        Note.add_note(note)


class DeleteNote(State):
    def update(self, note, note_id):
        pass

    def delete(self, note_id):
        pass

    def read(self, note):
        self.context.transition_to(ReadNote(), note, session['user_id'])

    def create(self, note, user):
        pass


class CreateNote(State):
    def update(self, note, note_id):
        pass

    def delete(self, note_id):
        pass

    def read(self, note):
        self.context.transition_to(ReadNote(), note, session['user_id'])

    def create(self, note, user):
        pass
