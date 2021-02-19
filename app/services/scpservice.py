from . import Setup

import scp


class SCPService(Setup):
    def __init__(self, ssh_client, local_path, remote_path=None):
        self.ssh_client = ssh_client
        self.local_path = local_path
        self.remote_path = remote_path

    def create_client(self):
        try:
            client = scp.SCPClient(self.ssh_client.get_transport())
            return client
        except Exception as e:
            print('Error al obtener archivo')
            return None

    def download_backup(self, client, db_bk_name):
        print('Descargando backup...')
        client.get(
            f'{db_bk_name}',
            f'{self.local_path}'
        )

    def run(self, db_bk_name):
        client = self.create_client()
        self.download_backup(client, db_bk_name)
        Setup.close_client(client)
