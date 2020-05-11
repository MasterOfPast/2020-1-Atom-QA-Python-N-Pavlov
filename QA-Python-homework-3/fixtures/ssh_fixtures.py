import pytest
from SSH_client.shh_client import SSH
from random import randint


@pytest.fixture()
def ssh_cl():
    with SSH(hostname='192.168.56.101', username='root',
             password='a1b2c3', port=2203) as ssh:
        yield ssh


@pytest.fixture(scope='class')
def nginx_data():
    return '192.168.56.101', 801


@pytest.fixture()
def random_name():
    return f'User-Agent{randint(5,100)}'
