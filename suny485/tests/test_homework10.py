import pytest

from suny485.projects.homework10.fruit_query import is_fruit


class TestHappyFruits(object):
    def test_fruit_apple(self):
        assert is_fruit('apple')

    def test_fruit_pear(self):
        assert is_fruit('pear')

    def test_fruit_bannana(self):
        assert is_fruit('bannana')

    def test_fruit_grape(self):
        assert is_fruit('grape')


class TestUnhappyFruits(object):
    def test_fruit_snapple(self):
        assert not is_fruit('snapple')

    def test_fruit_banana(self):
        assert not is_fruit('banana')

    def test_fruit_Pear(self):
        assert not is_fruit('Pear')

    def test_empty_str(self):
        assert not is_fruit('')

    def test_None(self):
        assert not is_fruit(None)

    def test_list(self):
        assert not is_fruit([])

    def test_no_arg(self):
        assert not is_fruit()
