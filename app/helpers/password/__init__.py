import hashlib


def generate_password(password):
    pswd = password.encode('utf-8')
    pswd_hash = hashlib.sha256(pswd)
    return pswd_hash.hexdigest()
