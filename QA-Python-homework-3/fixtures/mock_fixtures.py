import pytest
from random import randint
from tests import socket_client as sc
from mock import mock


@pytest.fixture(scope='session')
def server_data():
    server = mock.run_mock()
    server_host = server._kwargs['host']
    server_port = server._kwargs['port']

    yield server_host, server_port

    sc.request('GET', server_host, server_port, '/shutdown')


@pytest.fixture()
def generate_date():
    return {
        'name': f"name{randint(1, 20)}",
        'surname': f'surname{randint(1, 20)}',
        'password': f'hell{randint(1, 20)}',
        'secret': str(randint(10, 1000))
    }
