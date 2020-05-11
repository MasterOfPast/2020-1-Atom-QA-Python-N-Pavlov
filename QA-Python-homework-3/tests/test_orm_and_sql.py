import pytest
from Orm_builder import Builder
from models.models import Demon


class Test_Database:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, orm_client):
        self.mysql = orm_client
        self.builder = Builder(orm_client)

    def test_add_table(self):
        self.builder.create_table()
        self.builder.add()
        assert self.mysql.session.query(Demon).all()[0].Heavenly_name == 'Аббадон'
