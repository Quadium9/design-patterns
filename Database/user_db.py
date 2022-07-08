from model import UserModel
from app import db
from Database.hash import compare_hash, create_hash


class User(UserModel):
    def add_user(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def login_user(self):
        try:
            db_user: UserModel = db.session.query(UserModel).filter(UserModel.username == self.username).first()
            if compare_hash(self.password, db_user.password):
                return db_user
            return None
        except:
            return None
