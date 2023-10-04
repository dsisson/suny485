import pytest

from suny485.projects.hw10.fruit_query import is_fruit


"""
testable things
+ string (exact match for key)
+ string match but leading/trailing space
+ string case difference
+ string non-match
+ non-string (int, list, dict, bool)
+ no arg
+ multiple args

running these tests (from /Users/derek/dev/suny485/suny485):
>>> pytest tests/hw10 -k TestHappyFruits -v
tests/hw10/test_hw10.py::TestHappyFruits::test_fruit_apple PASSED                                        [ 25%]
tests/hw10/test_hw10.py::TestHappyFruits::test_fruit_pear PASSED                                         [ 50%]
tests/hw10/test_hw10.py::TestHappyFruits::test_fruit_bannana PASSED                                      [ 75%]
tests/hw10/test_hw10.py::TestHappyFruits::test_fruit_grape PASSED                                        [100%]

>>> pytest tests/hw10 -k TestUnhappyFruits -v
tests/hw10/test_hw10.py::TestUnhappyFruits::test_fruit_snapple PASSED                                    [ 14%]
tests/hw10/test_hw10.py::TestUnhappyFruits::test_fruit_banana PASSED                                     [ 28%]
tests/hw10/test_hw10.py::TestUnhappyFruits::test_fruit_Pear PASSED                                       [ 42%]
tests/hw10/test_hw10.py::TestUnhappyFruits::test_empty_str PASSED                                        [ 57%]
tests/hw10/test_hw10.py::TestUnhappyFruits::test_None PASSED                                             [ 71%]
tests/hw10/test_hw10.py::TestUnhappyFruits::test_list PASSED                                             [ 85%]
tests/hw10/test_hw10.py::TestUnhappyFruits::test_no_arg FAILED                                           [100%]
"""

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
        with pytest.raises(TypeError):
            assert not is_fruit()
