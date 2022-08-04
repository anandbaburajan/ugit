from asyncore import write
import os

from . import data


def write_tree(directory='.'):
    entries = []

    with os.scandir(directory) as it:
        for entry in it:
            full_path = f'{directory}/{entry.name}'
            oid = ''

            if is_ignored(full_path):
                continue

            if entry.is_file(follow_symlinks=False):
                type_ = 'blob'
                with open(full_path, 'rb') as f:
                    oid = data.hash_object(f.read())
            elif entry.is_dir(follow_symlinks=False):
                type_ = 'tree'
                oid = write_tree(full_path)

            entries.append((type_, oid, entry.name))

    tree = ''.join(f'{type_} {oid} {name}\n'
                   for type_, oid, name
                   in sorted(entries))

    return data.hash_object(tree.encode(), 'tree')


def is_ignored(path):
    return '.ugit' in path.split('/')
