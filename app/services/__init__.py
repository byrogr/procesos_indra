class Setup:
    def create_client(self):
        pass

    @staticmethod
    def run_command(client, cmd):
        stdin, stdout, stderr = client.exec_command(cmd)
        print(stdout.read().decode())
        print('Ok.')

    @staticmethod
    def close_client(client):
        print('Desconectado.')
        client.close()
