import pytest


class Test2:
    def test_set_1(self, static_set):
        with pytest.raises(KeyError):
            assert static_set.remove("z")

    def test_set_2(self, static_set):
        with pytest.raises(TypeError):
            print(static_set[-1])

    def test_set_3(self, static_set):
        result = static_set.copy()
        assert static_set == result

    @pytest.mark.parametrize("i", [set("Hello"), set("asdfghjklkjhf"),
                                   set("last test")])
    def test_set_4(self, i):
        i.clear()
        assert i == set()

    def test_set_5(self, static_set):
        assert 'a' in static_set
