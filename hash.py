import bcrypt


def create_hash(passwd):
    passwd = bytes(passwd, 'utf-8')
    return bcrypt.hashpw(passwd, bcrypt.gensalt())


def compare_hash(passwd, hashed_passwd):
    passwd = bytes(passwd, 'utf-8')
    return bcrypt.checkpw(passwd, bytes(hashed_passwd, 'utf-8'))

