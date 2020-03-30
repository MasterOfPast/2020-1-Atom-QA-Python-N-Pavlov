import pytest
from api.urls import Urls


class TestApi():
    @pytest.mark.API
    def test_auth(self, api_client, auth_data):
        location = api_client.redir_auth(*auth_data)
        assert location == Urls.good_url

    @pytest.mark.API
    def test_fail_auth(self, api_client, random_data):
        location = api_client.redir_auth(*random_data)
        assert location == Urls.bad_url

    @pytest.mark.API
    def test_create(self, api_client, create_data):
        api_client.login()
        response = api_client.create(create_data)
        assert response.status_code == 200

    @pytest.mark.API
    def test_delete(self, api_client, create_data):
        api_client.login()
        response = api_client.create(create_data)
        id = response.json()['id']
        status_code = api_client.delete(id)
        assert status_code == 204
