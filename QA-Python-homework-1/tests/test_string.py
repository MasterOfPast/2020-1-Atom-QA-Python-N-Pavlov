import pytest


class Test4:
    def test_string_1(self, static_string):
        assert static_string.isdigit() or not static_string.isdigit()

    @pytest.mark.parametrize("i", ["Hi", "123", "The 1", "qwerty"])
    def test_string_2(self, i):
        assert i.istitle() or not i.istitle()

    def test_string_3(self, random_string):
        assert random_string.isalnum() or not random_string.isalnum()

    def test_string_4(self, random_string):
        assert random_string[0] == "f" or random_string[0] != 'f'

    def test_string_5(self, random_string):
        assert "y" in random_string or "y" not in random_string
