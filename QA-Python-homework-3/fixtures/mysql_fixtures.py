import pytest
from mysql_client.client import MysqlOrmConnection


@pytest.fixture(scope='class')
def orm_client():
    return MysqlOrmConnection('root', 'kJShTB', 'Test_db')
