from decouple import config


class Config:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def get_config(self):
        return {
            'host': self.host,
            'user': self.user,
            'pass': self.password
        }


class DBConfig(Config):
    def __init__(self):
        Config.__init__(self, config('DB_HOST'), config('DB_HOST_USER'), config('DB_HOST_PASS'))
        self.db_user = config('DB_USER')
        self.db_pass = config('DB_PASS')


class FTPConfig(Config):
    def __init__(self):
        Config.__init__(self, config('FTP_HOST'), config('FTP_HOST_USER'), config('FTP_HOST_PASS'))
