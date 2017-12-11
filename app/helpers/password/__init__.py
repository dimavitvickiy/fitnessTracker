import hashlib


def generate_password(password):
    pswd = password.encode('utf-8')
    pswd_hash = hashlib.sha256(pswd)
    return pswd_hash.hexdigest()


def generate_password_first_mutation(password):
    pswd = password.encode('utf-8')
    pswd_hash = hashlib.sha256(pswd)
    return pswd_hash.digest()


def generate_password_second_mutation(password):
    pswd = password.encode('utf-8')
    pswd_hash = hashlib.md5(pswd)
    return pswd_hash.hexdigest()
