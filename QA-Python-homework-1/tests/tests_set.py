import pytest


class Test2:
    def test_set_1(self, static_set):
        assert len(static_set) > 4

    def test_set_2(self, static_set):
        assert len(static_set) < 7

    def test_set_3(self, static_set):
        assert static_set == set("aaabbcdee")

    @pytest.mark.parametrize("i", [set("Hello"), set("asdfghjklkjhf"),
                                   set("last test")])
    def test_set_4(self, i):
        assert len(i) == 5

    def test_set_5(self, static_set):
        assert static_set.intersection_update(set("zxcv")) is not None
