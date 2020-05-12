from sys import argv
import sys


class Build_sql:
    def __init__(self, connection):
        self.connection = connection
        self.engine = connection.connection.engine
        self.create_table()

    def create_table(self):
        if not self.engine.dialect.has_table(self.engine, 'logs_nginx'):
            Base.metadata.tables['logs_nginx'].create(self.engine)

    def add(self):
        param = argv[6].split()
        log = Log(
            ip=argv[1],
            date=argv[4][1:],
            method=param[0],
            request=param[1] + ' ' + param[2],
            status=int(argv[7]),
            body_bytes_sent=int(argv[8]),
            http_user_agent=argv[10]
        )
        self.connection.session.add(log)
        self.connection.session.commit()


def connect():
    return MysqlOrmConnection('root', 'kJShTB', 'Nginx_logs', delete_db=False)


if __name__ == '__main__':
    sys.path.append('../')
    from mysql_client.client import MysqlOrmConnection
    from models.models import Log, Base
    start = Build_sql(connect())
    start.add()
