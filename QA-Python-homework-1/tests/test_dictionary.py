import pytest


class Test3:
    def test_dict_1(self, static_dict):
        static_dict.clear()
        assert static_dict == {}

    def test_dict_2(self, static_dict):
        assert list(static_dict.keys())[0] in static_dict

    def test_dict_3(self, static_dict):
        assert list(static_dict.values())[1] in static_dict

    def test_dict_4(self, random_int):
        with pytest.raises(KeyError):
            dict_test = {"q": "we", "r": "ty", "ui": "o"}
            assert dict_test[random_int]

    @pytest.mark.parametrize("i", [{3: 2, 7: 8, 10: 12}, {2: 3},
                                   {3: 2, 7: 15}])
    def test_dict_5(self, i):
        if 3 in i:
            assert i.get(3) is not None
        else:
            assert i.get(3) is None
