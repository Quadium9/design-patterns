from abc import ABC, abstractmethod
from Database.note_db import Note
from Database.user_db import User
from Database.model import NoteModel, UserModel


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def create(self):
        creator = self.factory_method()
        return creator


class NoteCreator(Creator):
    def factory_method(self) -> Note:
        return NoteModel()


class UserCreator(Creator):
    def factory_method(self) -> User:
        return UserModel()
