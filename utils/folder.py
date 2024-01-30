import os
import pathlib
import stat
import subprocess

import click


def create_folder(path, mode):
    # pathlib.Path(f"./{path}").mkdir(mode=0o707)
    # folder_stat = os.stat(path)
    # folder_mode = folder_stat.st_mode & 0o777
    # print(folder_mode)
    # print(str(pathlib.Path(f"./{path}").absolute().resolve()))
    # subprocess.run(['chmod', '707', str(pathlib.Path(f"./{path}/").absolute())])
    # print(mode)
    # os.umask(0)
    # os.makedirs(f"./{path}", exist_ok=True)
    # os.chmod(f"./{path}", 0o707)
    original_umask = os.umask(0)
    try:
        os.makedirs(f"./{path}", 0o40444)
    finally:
        os.umask(original_umask)


def folder_permission(path):
    perm = pathlib.Path(f"./{path}").stat().st_mode
    click.echo(f'Permission for folder "{path}": {oct(perm)} ({stat.filemode(perm)})')
