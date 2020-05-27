import pytest
import string
import docker
from random import randint, choice
from sql_client.client import MysqlOrmConnection
from time import sleep
import os


@pytest.fixture(scope='session', autouse=True)
def docker_run():
    client = docker.from_env()
    container_mysql = client.containers.get('mysql1')
    container_mysql.start()
    sleep(2)
    container_vk = client.containers.get('vk')
    container_vk.start()
    sleep(2)
    container_app = client.containers.get('web_app')
    container_app.start()
    yield
    sleep(15)
    container_app.stop()
    container_mysql.stop()
    container_vk.stop()
    fixtures_path = os.path.dirname(__file__)
    path = os.path.join(fixtures_path, "..", "tmp", "allure")
    path = os.path.abspath(path)
    os.system(f'allure serve {path}')


@pytest.fixture(scope='session')
def auth_data():
    return {'user': 'Helloworld', 'password': 'hello', 'email': 'hello@m.net'}


@pytest.fixture(scope='session')
def second_auth_data():
    return ('enter_user', '123456')


@pytest.fixture()
def data_to_create():
    return {
        'user': f'Test_name{randint(1,10000)}',
        'password': f"{'a' * randint(1, 7)}#{'z' * randint(1, 10)}",
        'email': f"{choice(string.ascii_letters) * randint(3, 10) + choice(string.ascii_letters)}@{'f' * randint(1, 5)}.ku"
    }


@pytest.fixture()
def date_with_space():
    return f"{randint(0, 100)}       {randint(0, 100)}"


@pytest.fixture()
def sql_client():
    return MysqlOrmConnection('root', 'a1b2c3', 'app')


@pytest.fixture()
def special_user():
    return ('test_na_na', '123456')
