import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models.models import Base, test_users


class MysqlOrmConnection:

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = '192.168.99.100'
        self.port = 3306
        self.connection = self.get_connection()

        session = sessionmaker(bind=self.connection.engine,
                               autocommit=True,
                               autoflush=True,
                               enable_baked_queries=False,
                               expire_on_commit=True)
        self.session = session()

    def get_connection(self):
        engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}',
            encoding='utf8'
        )

        return engine.connect()

    def execute_query(self, query):
        res = self.connection.execute(query)
        return res.fetchall()

    def select(self, column, value):
        query = f'SELECT * FROM test_users WHERE {column}="{value}"'
        return self.execute_query(query)

    def delete(self, column, value):
        query = f'DELETE FROM test_users WHERE {column}="{value}"'
        return self.execute_query(query)

    def add(self, user, mail, password):
        user = test_users(
            username=user,
            password=password,
            email=mail,
            access=1
        )
        self.session.add(user)
