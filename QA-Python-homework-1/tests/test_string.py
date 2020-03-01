import pytest


class Test4:
    def test_string_1(self, static_string):
        assert not static_string.isdigit()

    @pytest.mark.parametrize("i", ["Hi", "123", "The 1", "Qwerty"])
    def test_string_2(self, i):
        if i[0].isalpha():
            assert i.istitle()
        else:
            with pytest.raises(AssertionError):
                assert i.istitle()

    def test_string_3(self, static_string):
        with pytest.raises(AssertionError):
            assert static_string.isalnum()

    def test_string_4(self, random_string):
        with pytest.raises(TypeError):
            random_string[0] = "b"

    def test_string_5(self, random_string):
        random_string += "y"
        assert "y" == random_string[-1]
