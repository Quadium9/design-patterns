from Database.model import UserModel
from app import db
from Database import hash


class User:
    @staticmethod
    def add_user(user_model):
        try:
            user_model.password = hash.create_hash(user_model.password)
            db.session.add(user_model)
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def login_user(user_model):
        try:
            db_user: UserModel = db.session.query(UserModel).filter(
                UserModel.username == user_model.username).first()
            if hash.compare_hash(user_model.password, db_user.password):
                return db_user
            return None
        except:
            return None
