import pytest


class Test5:
    def test_int_1(self, static_int):
        new_int = static_int << 1
        assert new_int == static_int * 2

    @pytest.mark.parametrize("i", list(range(8)))
    def test_int_2(self, i):
        new_int = i >> 1
        assert new_int == i // 2

    def test_int_3(self, random_int):
        result = divmod(random_int, 4)
        assert result[0] * 4 + result[1] == random_int

    def test_int_4(self, random_int):
        assert random_int ** 2 == random_int * random_int

    def test_int_5(self, random_int):
        assert random_int % 3 == 0 or random_int % 3 != 0
