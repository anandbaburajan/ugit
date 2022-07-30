import hashlib
import os


UGIT_DIR = '.ugit'


def init():
    os.makedirs(UGIT_DIR)
    os.makedirs(f'{UGIT_DIR}/objects')


def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    with open(f'{UGIT_DIR}/objects/{oid}', 'wb') as out:
        out.write(data)
    return oid


def get_object(oid):
    with open(f'{UGIT_DIR}/objects/{oid}', 'rb') as f:
        return f.read()
