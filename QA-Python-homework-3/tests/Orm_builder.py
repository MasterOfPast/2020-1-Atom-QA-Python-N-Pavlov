from models.models import Base, Demon
from faker import Faker


fake = Faker(locale='ru_RU')


class Builder:
    def __init__(self, connection):
        self.connection = connection
        self.engine = connection.connection.engine

    def create_table(self):
        if not self.engine.dialect.has_table(self.engine, 'demons'):
            Base.metadata.tables['demons'].create(self.engine)

    def add(self):
        demon = Demon(
            name='Владыка грязи',
            Heavenly_name='Аббадон',
            True_name="^^&**&#fgha@nn!!",
            reliase_date=fake.date()
        )
        self.connection.session.add(demon)
        self.connection.session.commit()
        return demon
