from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, TINYTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class NoteModel(Base):
    __tablename__ = 'note'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(64, 'utf8mb3_polish_ci'))
    create_date = Column(DateTime)
    planned_date = Column(DateTime)
    description = Column(TINYTEXT)
    active = Column(INTEGER(11))
    user_id = Column(ForeignKey('user.id'), index=True)

    user = relationship('UserModel')

    def __init__(self, title, create_date, description, user_id, active, planned_date):
        self.title = title
        self.create_date = create_date
        self.description = description
        self.user_id = user_id
        self.active = active
        self.planned_date = planned_date


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(INTEGER(11), primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(256), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
