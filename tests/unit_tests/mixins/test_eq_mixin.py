from sylenium.mixins import SimpleEQMixin


class Dummy(SimpleEQMixin):
    def __init__(self, x: int = 0):
        self.x = x


def test_eq_matches():
    assert Dummy(5) == Dummy(5)


def test_eq_fails_matching():
    assert Dummy(5) != Dummy(4)
