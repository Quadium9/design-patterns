import datetime
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
    def __init__(self, note: str, active: bool, title: str):
        self.active = active
        self.title = title
        self.note = note

    def factory_method(self) -> Note:
        return NoteModel(title=self.title,
                         note=self.note,
                         create_date=datetime.date.today(),
                         user_id='',
                         active=self.active)


class UserCreator(Creator):
    def __init__(self, password: str, username: str):
        self.password = password
        self.username = username

    def factory_method(self) -> UserModel:
        return UserModel(username=self.username,
                         password=self.password)
