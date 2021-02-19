from fabric.api import run


def show_dir():
    run('ls -la')


def backup(db_name):
    pass