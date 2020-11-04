import hashlib
def get_md5(username,passowrd):
    md5 = hashlib.md5(username.encode('utf-8'))
    md5.update(passowrd.encode('utf-8'))
    return md5.hexdigest()

ret = get_md5('alex','3714')
print(ret)