import pytest


class Test1:
    def test_list_1(self, static_list):
        assert sum(static_list) == 10

    @pytest.mark.parametrize("i", [[1, 2, 5], [3, 4, 5, 6], [2, 3, 6]])
    def test_list_2(self, i):
        assert 2 in i or 2 not in i

    def test_list_3(self, static_list):
        element = static_list[-1]
        static_list.reverse()
        assert element == static_list[0]

    def test_list_4(self, random_list):
        assert random_list[0] == 2 or random_list[0] != 2

    def test_list_5(self, random_list):
        assert random_list.count(10) == 1 or random_list.count(10) != 1