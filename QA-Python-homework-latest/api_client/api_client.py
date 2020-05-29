import requests
from urllib.parse import urljoin
import json


class Client:
    def __init__(self, user, password, config):
        self.user = user
        self.password = password
        self.url = config['url']
        self.session = requests.Session()
        self.headers = {
            'Cookie': self.get_session().headers['Set-Cookie']
        }

    def _request(self, method, location, headers=None, data=None,
                 redirect=False):
        url = urljoin(self.url, location)
        response = self.session.request(method, url, headers=headers,
                                        data=data, allow_redirects=redirect)
        return response

    def get_session(self):
        request = self._request("POST", 'login', data={
            'username': self.user,
            'password': self.password,
            'submit': 'Login'
        })
        return request

    def add(self, data_to_create):
        headers = self.headers
        headers["Content-Type"] = 'application/json'
        self.h = headers
        self.u = data_to_create['user']
        self.p = data_to_create['password']
        responce = self._request("POST", 'api/add_user', data=json.dumps({
            'username': data_to_create['user'],
            'email': data_to_create['email'],
            'password': data_to_create['password']
        }), headers=headers)
        return responce

    def delete(self, user):
        response = self._request("GET", f'api/del_user/{user}',
                                 headers=self.headers)
        return response

    def lock(self, user):
        response = self._request("GET", f'api/block_user/{user}',
                                 headers=self.headers)
        return response

    def unlock(self, user):
        response = self._request("GET", f'api/accept_user/{user}',
                                 headers=self.headers)
        return response


def status(config):
    return requests.get(config['url'] + 'status').json()
