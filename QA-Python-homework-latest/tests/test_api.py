from api_client.api_client import status
import pytest
import allure


class Test_Api:
    @pytest.fixture(autouse=True)
    def setup(self, norm_auth, special_auth):
        self.client = norm_auth
        self.special_client = special_auth

    @allure.story('main')
    @pytest.mark.main
    def test_status(self, config):
        """Проверка через API, что приложение работает"""
        assert status(config)['status'] == 'ok'

    @allure.story('main')
    @pytest.mark.main
    def test_add(self, data_to_create, sql_client):
        """Проверка создания пользователя через API"""
        request = self.client.add(data_to_create)
        print(sql_client.select('username', data_to_create['user']))
        password = sql_client.select('username', data_to_create['user'])[0][2]
        assert password == data_to_create['password']
        status_code = request.status_code
        assert status_code == 201

    @allure.story('other')
    @pytest.mark.other
    def test_exist_user_add(self, auth_data, data_to_create, sql_client):
        """Проверка, что через API пользователь с существующим именем
        не создастся"""
        assert self.client.add({
            'user': auth_data['user'],
            'password': data_to_create['password'],
            'email': data_to_create['email']
        }).status_code == 304
        assert sql_client.select('password', data_to_create['email']) == []

    @allure.story('other')
    @pytest.mark.other
    def test_exist_email_add(self, auth_data, data_to_create, sql_client):
        """Проверка, что через API пользователь с существующим email
        не создастся"""
        status_code = self.client.add({
            'user': data_to_create['user'],
            'password': data_to_create['password'],
            'email': auth_data['email']
        }).status_code
        assert sql_client.select('username', data_to_create['user']) == []
        assert status_code == 304

    @allure.story('other')
    @pytest.mark.other
    def test_void_add(self, sql_client):
        """Проверка, добавления через API абсолютно пустого пользователя"""
        if sql_client.select('username', '') != []:
            try:
                sql_client.delete('username', '')
            except Exception:
                pass
        status_code = self.client.add({
            'user': '',
            'password': '',
            'email': ''
        }).status_code
        assert sql_client.select('username', '') == []
        assert status_code == 400

    @allure.story('other')
    @pytest.mark.other
    def test_hell_add(self, data_to_create, sql_client):
        """Проверка реакции на создание пользователя с невозможно
        длинным именем"""
        request = self.client.add({
            'user': 'a' * 256,
            'password': data_to_create['password'],
            'email': data_to_create['email']
        })
        assert sql_client.select('email', data_to_create['email']) == []
        assert request.status_code == 400

    @allure.story('other')
    @pytest.mark.other
    def test_hell_add_password(self, data_to_create, sql_client):
        """Проверка реакции приложения на создание пользователя
        с невозможно длинным паролем"""
        request = self.client.add({
            'user': data_to_create['user'],
            'password': 'a' * 256,
            'email': data_to_create['email']
        })
        assert sql_client.select('username', data_to_create['user']) == []
        assert request.status_code == 400

    @allure.story('other')
    @pytest.mark.other
    def test_hell_add_email(self, data_to_create, sql_client):
        """Проверка реакции приложения на создание пользователя
        с невозможно длинным email"""
        request = self.client.add({
            'user': data_to_create['user'],
            'password': '',
            'email': 'a' * 256})
        assert sql_client.select('username', data_to_create['user']) == []
        assert request.status_code == 400

    @allure.story('other')
    @pytest.mark.other
    def test_delete(self, data_to_create, sql_client):
        """Проверка удаления пользователя через API"""
        self.client.add(data_to_create)
        request = self.client.delete(data_to_create['user'])
        assert request.status_code == 204
        assert sql_client.select('username', data_to_create['user']) == []

    @allure.story('other')
    @pytest.mark.other
    def test_fail_delete(self):
        """Проверка реакции на попытку через API удалить несуществующего
        пользователя"""
        request = self.client.delete('fail_name')
        assert request.text == 'User does not exist!'
        assert request.status_code == 404

    @allure.story('other')
    @pytest.mark.other
    def test_hell_delete(self):
        """Проверка реакции на попытку через API удалить несуществующего
        пользователя с невозможно длинным именем"""
        request = self.client.delete('a' * 256)
        assert request.text == 'User does not exist!'
        assert request.status_code == 404

    @allure.story('other')
    @pytest.mark.other
    def test_lock(self, data_to_create, sql_client):
        """Проверка блокировки пользователя через API"""
        self.client.add(data_to_create)
        request = self.client.lock(data_to_create['user'])
        assert sql_client.select('username', data_to_create['user'])[0][4] == 0
        assert request.status_code == 200
        assert request.text == 'User was blocked!'
        try:
            sql_client.delete('username', data_to_create['user'])
        except Exception:
            pass

    @allure.story('other')
    @pytest.mark.other
    def test_two_lock(self, data_to_create, sql_client):
        """Проверка двойной блокировки пользователя через API"""
        self.client.add(data_to_create)
        self.client.lock(data_to_create['user'])
        request = self.client.lock(data_to_create['user'])
        assert request.status_code == 304
        try:
            sql_client.delete('username', data_to_create['user'])
        except Exception:
            pass

    @allure.story('other')
    @pytest.mark.other
    def test_fail_lock(self):
        """Проверка реакции на попытку блокировки несуществующего
        пользователя"""
        request = self.client.lock("fail_name")
        assert request.status_code == 404
        assert request.text == 'User does not exist!'

    @allure.story('other')
    @pytest.mark.other
    def test_hell_lock(self):
        """Проверка реакции на попытку блокировки несуществующего
        пользователя с невозможно длинным именем"""
        request = self.client.lock("a" * 256)
        assert request.status_code == 404
        assert request.text == 'User does not exist!'

    @allure.story('other')
    @pytest.mark.other
    def test_unlock(self):
        """Проверка разблокировки пользователя через api"""
        self.client.lock('norm_name')
        request = self.client.unlock("norm_name")
        assert request.status_code == 200
        assert request.text == 'User access granted!'

    @allure.story('other')
    @pytest.mark.other
    def test_fail_unlock(self):
        """Проверка, разблокировки несуществующего пользователя"""
        request = self.client.unlock("fail_name")
        assert request.status_code == 404
        assert request.text == 'User does not exist!'

    @allure.story('other')
    @pytest.mark.other
    def test_hell_unlock(self):
        """Проверка, разблокировки несуществующего пользователя
        невозможной длины"""
        request = self.client.unlock("a" * 256)
        assert request.status_code == 404
        assert request.text == 'User does not exist!'

    @allure.story('other')
    @pytest.mark.other
    def test_self_lock(self):
        """Проверка, что заблокированный пользователь не смотря на печеньки
        через API ничего не сможет делать"""
        self.client.unlock('test_name')
        self.special_client.lock('test_name')
        assert self.special_client.unlock('test_name').status_code == 401

    @allure.story('other')
    @pytest.mark.other
    def test_lock_locked(self, data_to_create):
        """Проверка разблокировки незаблокированного пользователя"""
        self.client.add(data_to_create)
        request = self.client.unlock(data_to_create['user'])
        assert request.status_code == 304
        self.client.delete(data_to_create['user'])
