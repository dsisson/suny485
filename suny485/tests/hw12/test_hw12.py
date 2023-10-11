import pytest

from suny485.projects.hw12.homework12 import compute_complexity


"""
testable things for projects.hw12.homework12.py::compute_complexity()
    + string
        + complexity correctly computed
            + without complexifier chars, should be 0.0
            + with complexifier chars, score depends on proportion of c-chars to length
            + all c-chars are the same
    + other data types
        + int
        + list
        + bool
        + dict
"""


class TestComplexityLogic(object):

    @pytest.mark.parametrize('good_input', [
        # no complexity
        ('password', 0.0),
        ('pa55word', 0.0),

        # all the same char
        ('&&&&&&&&', 100.0),

        # proportions
        ('a', 0.0),
        ('a%', 50.0),
        ('ab%', 33.333333333333336),
        ('abc%', 25.0),
        ('abcd%', 20.0),
        ('abcde%', 16.666666666666668),

        # increasing complexity for 8char strings
        ('_assword', 12.5),
        ('_@ssword', 25.0),
        ('_@#sword', 37.5),
        ('_@#-word', 50.0),
        ('_@#-%ord', 62.5),
        ('_@#-%=rd', 75.0),
        ('_@#-%=-d', 87.5),
        ('_@#-%=-^', 100.0),

        # increasing complexity for 9char strings
        ('passwords', 0.0),
        ('_asswords', 11.11111111111111),
        ('_@sswords', 22.22222222222222),
        ('_@#swords', 33.333333333333336),
        ('_@#-words', 44.44444444444444),
        ('_@#-%ords', 55.55555555555556),
        ('_@#-%=rds', 66.66666666666667),
        ('_@#-%=-ds', 77.77777777777777),
        ('_@#-%=-^s', 88.88888888888889),
        ('_@#-%=-^~', 100.0),

        # increasing complexity for 10char strings
        ('mypassword', 0.0),
        ('$ypassword', 10.0),
        ('$$password', 20.0),
        ('$$$assword', 30.0),
        ('$$$$ssword', 40.0),
        ('$$$$$sword', 50.0),
        ('$$$$$$word', 60.0),
        ('$$$$$$$ord', 70.0),
        ('$$$$$$$$rd', 80.0),
        ('$$$$$$$$$d', 90.0),
        ('$$$$$$$$$$', 100.0),
    ], ids=[
        'password',
        'pa55word',
        '&&&&&&&&',
        'a',
        'a%',
        'ab%',
        'abc%',
        'abcd%',
        'abcde%',
        '_assword',
        '_@ssword',
        '_@#sword',
        '_@#-word',
        '_@#-%ord',
        '_@#-%*rd',
        '_@#-%*-d',
        '_@#-%*-^',
        'passwords',
        '_asswords',
        '_@sswords',
        '_@#swords',
        '_@#-words',
        '_@#-%ords',
        '_@#-%=rds',
        '_@#-%=-ds',
        '_@#-%=-^s',
        '_@#-%=-^~',
        'mypassword',
        '$ypassword',
        '$$password',
        '$$$assword',
        '$$$$ssword',
        '$$$$$sword',
        '$$$$$$word',
        '$$$$$$$ord',
        '$$$$$$$$rd',
        '$$$$$$$$$d',
        '$$$$$$$$$$',
    ])
    def test_complexity_for_valid_str(self, good_input):
        data, expected_complexity = good_input
        assert compute_complexity(data) == expected_complexity

    @pytest.mark.parametrize('bad_input', [
        # other data types
        (42, 0.0),
        (True, 0.0),
    ], ids=[
        'int',
        'bool',
    ])
    def test_complexity_for_invalid_arg(self, bad_input):
        data, expected_complexity = bad_input
        assert compute_complexity(data) == expected_complexity

    @pytest.mark.xfail
    @pytest.mark.parametrize('should_fail', [
        # other data types
        ([1, 2], 0.0),
        ({1, 2, 3}, 0.0),
        ({'foo': 'bar'}, 0.0),
    ], ids=[
        'list',
        'tuple',
        'dict'
    ])
    def test_complexity_for_invalid_arg_that_should_fail(self, should_fail):
        data, expected_complexity = should_fail
        assert compute_complexity(data) == expected_complexity
