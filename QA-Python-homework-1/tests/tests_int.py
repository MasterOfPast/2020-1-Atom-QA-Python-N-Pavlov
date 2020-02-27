import pytest


class Test5:
    def test_int_1(self, static_int):
        assert abs(static_int) > 100

    @pytest.mark.parametrize("i", list(range(8)))
    def test_int_2(self, i):
        assert i < 4

    def test_int_3(self, random_int):
        assert random_int < 50

    def test_int_4(self, random_int):
        assert random_int > -50

    def test_int_5(self, random_int):
        assert random_int % 3 == 0
