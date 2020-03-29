from urllib.parse import urljoin

import requests
import json
from api.urls import Urls


class ResponseStatusCodeException(Exception):
    pass


class Client:
    def __init__(self, user, password):
        self.base_url = 'https://target.my.com/'
        self.session = requests.Session()
        self.user = user
        self.password = password

    def _request(self, method, location, headers=None, params=None, data=None, json=True):
            url = urljoin(self.base_url, location)

            response = self.session.request(method, url, headers=headers, params=params, data=data)

            if json:
                response = response.json()

            return response

    def login(self):
        location = Urls.auth_url
        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1#email',
            'failure': 'https://account.my.com/login/'
        }
        response = self.session.request('POST', location, data=data)
        return response.text

    def au(self):
        location = 'https://auth-ac.my.com/auth'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Cache-Control': 'max-age=0',
            "Host": 'auth-ac.my.com',
            "Content-Type": "application/x-www-form-urlencoded",
            'Accept-Encoding': 'gzip, deflate, br',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        params = {
            'lang': 'ru',
            'nosavelogin': 0
        }
        data = {
            'email': self.login,
            'password': self.password
        }
        #response = self.session.request("GET", "https://target.my.com/")
        response = self.session.request('POST', Urls.auth_url, data=data, headers=headers)
        return response.url