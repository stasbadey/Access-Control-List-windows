import subprocess


def operation_group(name, operation):
    subprocess.run(['net', 'localgroup', name, f'/{operation}'])
