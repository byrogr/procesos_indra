from . import Setup
from .scpservice import SCPService
from app.config import DBConfig
from app.utils import get_backup_name

import paramiko


class DBService(Setup):
    def __init__(self, db_name):
        self.db_config = DBConfig()
        self.config = self.db_config.get_config()
        # self.client = self.create_client()
        self.db_name = db_name

    def create_client(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.config.get('host'), username=self.config.get('user'), password=self.config.get('pass'))
            print('Conectado.')
            return client
        except paramiko.ssh_exception.AuthenticationException as e:
            print('No se pudo conectar al servidor')
            return None

    def create_backup(self, client, db_bk_name):
        print("Preparando backup ...\n")
        cmd = f'mysqldump -u {self.db_config.db_user} -p{self.db_config.db_pass} {self.db_name} > {db_bk_name}'
        Setup.run_command(client, cmd)

    def delete_backup(self, client, db_bk_name):
        print("Eliminando backup ...")
        cmd = f'rm {db_bk_name}'
        Setup.run_command(client, cmd)

    def run(self):
        print("Conectando con el servidor ...")

        client = self.create_client()
        scp_client = SCPService(client, 'D:\db_backups')
        db_bk_name = get_backup_name(self.db_name)
        self.create_backup(client, db_bk_name)
        # self.delete_backup(client, db_bk_name)
        scp_client.run(db_bk_name)
        print("Desconectando con el servidor ...")
        Setup.close_client(client)
