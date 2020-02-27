import pytest


class Test3:
    def test_dict_1(self, static_dict):
        assert len(static_dict) < 3

    def test_dict_2(self, static_dict):
        assert len(static_dict) > 1

    def test_dict_3(self, static_dict):
        assert static_dict['test'] is not None

    def test_dict_4(self, random_dict):
        assert random_dict[5] > 0

    @pytest.mark.parametrize("i", [{3: 2, 7: 8, 10: 12}, {2: 6},
                                   {3: 2, 7: 15}])
    def test_dict_5(self, i):
        assert 3 in i
