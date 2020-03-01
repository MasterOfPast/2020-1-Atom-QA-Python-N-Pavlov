import pytest


class Test1:
    def test_list_1(self, static_list):
        assert sum(static_list) == 10

    @pytest.mark.parametrize("i", [[1, 2, 5], [3, 4, 5, 9], [7, 3, 6]])
    def test_list_2(self, i):
        if 2 in i:
            assert i.index(2) is not None
        else:
            with pytest.raises(ValueError):
                assert i.index(2) is not None

    def test_list_3(self, static_list):
        element = static_list[-1]
        static_list.reverse()
        assert element == static_list[0]

    def test_list_4(self, random_list):
        random_list.append(2)
        assert random_list[-1] == 2

    def test_list_5(self, random_list):
        with pytest.raises(IndexError):
            k = random_list[len(random_list)]
            assert k is not None
