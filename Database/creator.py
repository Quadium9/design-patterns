import datetime
from abc import ABC, abstractmethod
from Database.model import NoteModel, UserModel


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def create(self):
        creator = self.factory_method()
        return creator


class NoteCreator(Creator):
    def __init__(self, note_form, user_id):
        self.note_form = note_form
        self.user_id = user_id

    def factory_method(self) -> NoteModel:
        return NoteModel(title=self.note_form.title.data,
                         description=self.note_form.description.data,
                         create_date=datetime.date.today(),
                         user_id=self.user_id,
                         active=1,
                         planned_date=self.note_form.date_field.data)


class UserCreator(Creator):
    def __init__(self, password: str, username: str):
        self.password = password
        self.username = username

    def factory_method(self) -> UserModel:
        return UserModel(username=self.username,
                         password=self.password)
