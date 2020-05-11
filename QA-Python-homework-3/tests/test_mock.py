import pytest
from socket_client import request
from mock.mock import users
import json


class Test:
    def test_add(self, server_data, generate_date):
        host, port = server_data
        result = request('POST', host, port, '/users/add', data=generate_date)
        assert result.status_code == 200

    def test_find(self, server_data, generate_date):
        host, port = server_data
        result = request('POST', host, port, '/users/add', data=generate_date)
        result = request('GET', host, port, f'/user/{len(users)}')
        assert json.loads(result.data)['name'] == generate_date['name']

    def test_enter(self, server_data, generate_date):
        host, port = server_data
        result = request('POST', host, port, '/users/add', data=generate_date)
        result = request('POST', host, port, '/users/enter', data={'id': str(len(users)),'password': generate_date['password']})
        assert json.loads(result.data)['secret'] == generate_date['secret']

    def test_enter_false(self, server_data, generate_date):
        host, port = server_data
        result = request('POST', host, port, '/users/add', data=generate_date)
        result = request('POST', host, port, '/users/enter', data={'id': '2', 'password': '1'})
        assert result.status_code == 400
