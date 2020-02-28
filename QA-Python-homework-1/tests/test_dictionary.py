import pytest


class Test3:
    def test_dict_1(self, static_dict):
        static_dict.clear()
        assert static_dict == {}

    def test_dict_2(self, static_dict):
        assert list(static_dict.keys())[0] in static_dict

    def test_dict_3(self, static_dict):
        assert list(static_dict.values())[1] in static_dict

    def test_dict_4(self, random_dict):
        assert random_dict[5] > 0 or random_dict[5] <= 0

    @pytest.mark.parametrize("i", [{3: 2, 7: 8, 10: 12}, {2: 6},
                                   {3: 2, 7: 15}])
    def test_dict_5(self, i):
        assert 3 in i or 3 not in i
