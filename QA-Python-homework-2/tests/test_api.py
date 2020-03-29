import pytest


class TestApi():
    @pytest.mark.API
    def test_auth(self, api_client):
        auth = api_client.au()
        print(auth)
