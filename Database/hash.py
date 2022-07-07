import bcrypt


def create_hash(passwd):
    passwd = bytes(passwd, 'utf-8')
    return bcrypt.hashpw(passwd, bcrypt.gensalt())


def compare_hash(password_from_forms, hashed_passwd):
    passwd = bytes(password_from_forms, 'utf-8')
    return bcrypt.checkpw(passwd, bytes(hashed_passwd, 'utf-8'))

