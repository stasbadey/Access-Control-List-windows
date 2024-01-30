import subprocess


def add_user(name, password):
    subprocess.run(['net', 'user', name, password, '/add'])


def delete_user(name):
    subprocess.run(['net', 'user', name, '/delete'])


def user_operation_group(group_name, user_name, operation):
    subprocess.run(['net', 'localgroup', group_name, user_name, f'/{operation}'])


def give_admin_user(name, operation):
    subprocess.run(['net', 'localgroup', 'Администраторы', name, f'/{operation}'])
