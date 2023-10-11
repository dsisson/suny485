import pytest

from suny485.projects.hw11.homework11 import get_formal_name_original
from suny485.projects.hw11.homework11 import get_formal_name_improved

good_keys = [
    'apple',
    'banana',
    'orange',
    'strawberry',
    'grape',
    'pineapple',
    'mango',
    'blueberry',
    'peach',
    'watermelon',
    'cherry',
    'pear',
    'plum',
    'raspberry',
    'kiwi',
    'lemon',
    'avocado',
    'pomegranate',
    'cranberry',
    'grapefruit'
]


valid_fruits = {
    'apple': 'Malus domestica',
    'banana': 'Musa acuminata',
    'orange': 'Citrus × sinensis',
    'strawberry': 'Fragaria × ananassa',
    'grape': 'Vitis vinifera',
    'pineapple': 'Ananas comosus',
    'mango': 'Mangifera indica',
    'blueberry': 'Vaccinium corymbosum',
    'peach': 'Prunus persica',
    'watermelon': 'Citrullus lanatus',
    'cherry': 'Prunus avium',
    'pear': 'Pyrus',
    'plum': 'Prunus domestica',
    'raspberry': 'Rubus idaeus',
    'kiwi': 'Actinidia deliciosa',
    'lemon': 'Citrus limon',
    'avocado': 'Persea americana',
    'pomegranate': 'Punica granatum',
    'cranberry': 'Vaccinium macrocarpon',
    'grapefruit': 'Citrus × paradisi'
}


class TestOriginalHappyFruits(object):

    @pytest.mark.parametrize('original_happy', good_keys)
    def test_good_key(self, original_happy):
        # setup
        this_key = original_happy
        print(f"--> {this_key}")
        expected_value = valid_fruits[this_key]
        assert get_formal_name_original(this_key) == expected_value


class TestOriginalUnhappyFruits(object):

    @pytest.mark.parametrize('original_unhappy', [
        '',
        ' banana',
        'banana ',
        'Peach',
        'foo'
    ])
    def test_bad_key(self, original_unhappy):
        # setup
        this_bad_key = original_unhappy

        with pytest.raises(KeyError):
            assert get_formal_name_original(this_bad_key)


class TestOriginalErrors(object):

    @pytest.mark.parametrize('original_key_error', [
        56,
        True,
    ])
    def test_problem_key_raises_key_error(self, original_key_error):
        # setup
        this_bad_key = original_key_error

        with pytest.raises(KeyError):
            assert get_formal_name_original(original_key_error)

    @pytest.mark.parametrize('original_type_error', [
        ['banana'],
        {1: 'banana'},
        'no args',
        '2 args',
    ], ids=[
        'list',
        'dict',
        'no args',
        '2 args',
    ])
    def test_problem_key_raises_key_error(self, original_type_error):
        # setup
        this_bad_key = original_type_error

        with pytest.raises(TypeError):
            if this_bad_key == 'no args':
                # special case
                assert get_formal_name_original()
            elif this_bad_key == '2 args':
                # special case
                assert get_formal_name_original('banana', 'plum')
            else:
                assert get_formal_name_original(this_bad_key)


# ## improved app code tests
class TestImprovedHappyFruits(object):

    @pytest.mark.parametrize('original_happy', good_keys)
    def test_good_key(self, original_happy):
        # setup
        this_key = original_happy
        print(f"--> {this_key}")
        expected_value = valid_fruits[this_key]
        assert get_formal_name_improved(this_key) == expected_value


class TestImprovedUnhappyFruits(object):

    @pytest.mark.parametrize('original_unhappy', [
        '',
        ' banana',
        'banana ',
        'Peach',
        'foo'
    ])
    def test_bad_key(self, original_unhappy):
        # setup
        this_bad_key = original_unhappy

        with pytest.raises(KeyError):
            assert get_formal_name_improved(this_bad_key)


class TestImprovedErrors(object):

    @pytest.mark.parametrize('original_key_error', [
        56,
        True,
    ])
    def test_problem_key_raises_key_error(self, original_key_error):
        # setup
        this_bad_key = original_key_error

        with pytest.raises(KeyError):
            assert get_formal_name_improved(this_bad_key)

    @pytest.mark.parametrize('original_type_error', [
        ['banana'],
        {1: 'banana'},
        'no args',
        '2 args',
    ], ids=[
        'list',
        'dict',
        'no args',
        '2 args',
    ])
    def test_problem_key_raises_key_error(self, original_type_error):
        # setup
        this_bad_key = original_type_error

        with pytest.raises(TypeError):
            if this_bad_key == 'no args':
                # special case
                assert get_formal_name_improved()
            elif this_bad_key == '2 args':
                # special case
                assert get_formal_name_improved('banana', 'plum')
            else:
                assert get_formal_name_improved(this_bad_key)
