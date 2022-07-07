from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, TINYTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from flask_login import UserMixin

Base = declarative_base()
metadata = Base.metadata


class NoteModel(Base):
    __tablename__ = 'note'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(64, 'utf8mb3_polish_ci'))
    create_date = Column(DateTime)
    planned_date = Column(DateTime)
    description = Column(TINYTEXT)
    user_id = Column(ForeignKey('user.id'), index=True)

    user = relationship('UserModel')


class UserModel(Base, UserMixin):
    __tablename__ = 'user'

    id = Column(INTEGER(11), primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(256), nullable=False)

