from datetime import datetime


def get_backup_name(db_name):
    return f'{db_name}_{ datetime.now().strftime("%d_%m_%Y")}_bk.sql'
