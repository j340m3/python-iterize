
from iterize import longest
from iterize.cli import main


def test_main():
    assert main([]) == 0


def test_longest():
    assert longest([b'a', b'bc', b'abc']) == b'abc'
