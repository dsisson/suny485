import pytest

from suny485.projects.hw11.homework11 import get_formal_name_original
from suny485.projects.hw11.homework11 import get_formal_name_improved

"""
testable things for get_formal_name_original
+ string (exact match for key)
+ string match but leading/trailing space
+ string case difference
+ string non-match
+ non-string (int, list, dict, bool)
+ no arg
+ multiple args

running these tests (from /Users/derek/dev/suny485/suny485):
>>> pytest tests/hw11 -k TestOriginalHappyFruits -v
tests/hw11/test_hw11.py::TestOriginalHappyFruits::test_banana PASSED                [ 33%]
tests/hw11/test_hw11.py::TestOriginalHappyFruits::test_peach PASSED                 [ 66%]
tests/hw11/test_hw11.py::TestOriginalHappyFruits::test_lemon PASSED                 [100%]

>>> pytest tests/hw11 -k TestOriginalUnhappyFruits -v
tests/hw11/test_hw11.py::TestOriginalUnhappyFruits::test_empty_string PASSED        [ 20%]
tests/hw11/test_hw11.py::TestOriginalUnhappyFruits::test_leading_space PASSED       [ 40%]
tests/hw11/test_hw11.py::TestOriginalUnhappyFruits::test_trailing_space PASSED      [ 60%]
tests/hw11/test_hw11.py::TestOriginalUnhappyFruits::test_case_difference PASSED     [ 80%]
tests/hw11/test_hw11.py::TestOriginalUnhappyFruits::test_non_matching_string PASSED [100%]

>>> pytest tests/hw11 -k TestOriginalErrors -v
tests/hw11/test_hw11.py::TestOriginalErrors::test_not_a_string_int PASSED           [ 16%]
tests/hw11/test_hw11.py::TestOriginalErrors::test_not_a_string_list PASSED          [ 33%]
tests/hw11/test_hw11.py::TestOriginalErrors::test_not_a_string_dict PASSED          [ 50%]
tests/hw11/test_hw11.py::TestOriginalErrors::test_not_a_string_bool PASSED          [ 66%]
tests/hw11/test_hw11.py::TestOriginalErrors::test_no_arg PASSED                     [ 83%]
tests/hw11/test_hw11.py::TestOriginalErrors::test_multiple_args PASSED              [100%]
"""


class TestOriginalHappyFruits(object):

    def test_banana(self):
        assert get_formal_name_original('banana') == 'Musa acuminata'

    def test_peach(self):
        assert get_formal_name_original('peach') == 'Prunus persica'

    def test_lemon(self):
        assert get_formal_name_original('lemon') == 'Citrus limon'


class TestOriginalUnhappyFruits(object):

    def test_empty_string(self):
        with pytest.raises(KeyError):
            assert get_formal_name_original('') == 'Musa acuminata'

    def test_leading_space(self):
        with pytest.raises(KeyError):
            assert get_formal_name_original(' banana') == 'Musa acuminata'

    def test_trailing_space(self):
        with pytest.raises(KeyError):
            assert get_formal_name_original('banana ') == 'Musa acuminata'

    def test_case_difference(self):
        with pytest.raises(KeyError):
            assert get_formal_name_original('Peach') == 'Prunus persica'

    def test_non_matching_string(self):
        with pytest.raises(KeyError):
            assert get_formal_name_original('ananab') == 'Musa acuminata'


class TestOriginalErrors(object):

    def test_not_a_string_int(self):
        # throws KeyError
        with pytest.raises(KeyError):
            assert get_formal_name_original(56) == 'Musa acuminata'

    def test_not_a_string_list(self):
        # throws TypeError
        with pytest.raises(TypeError):
            assert get_formal_name_original(['banana']) == 'Musa acuminata'

    def test_not_a_string_dict(self):
        # throws TypeError
        with pytest.raises(TypeError):
            assert get_formal_name_original({1: 'banana'}) == 'Musa acuminata'

    def test_not_a_string_bool(self):
        # throws KeyError
        with pytest.raises(KeyError):
            assert get_formal_name_original(True) == 'Musa acuminata'

    def test_no_arg(self):
        # no args is not allowed
        # throws TypeError
        with pytest.raises(TypeError):
            assert get_formal_name_original() == 'Musa acuminata'

    def test_multiple_args(self):
        # 2 args is not allowed
        # throws TypeError
        with pytest.raises(TypeError):
            assert get_formal_name_original('banana', 'plum') == 'Musa acuminata'


"""
testable things for get_formal_name_improved
+ string (exact match for key or case variations)
+ string match but leading/trailing space
+ string non-match
+ non-string (int, list, dict, bool)
+ no arg
+ multiple args

running these tests (from /Users/derek/dev/suny485/suny485):
>>> pytest tests/hw11 -k TestImprovedHappyFruits -v
tests/hw11/test_hw11.py::TestImprovedHappyFruits::test_banana PASSED                [ 25%]
tests/hw11/test_hw11.py::TestImprovedHappyFruits::test_peach PASSED                 [ 50%]
tests/hw11/test_hw11.py::TestImprovedHappyFruits::test_lemon PASSED                 [ 75%]
tests/hw11/test_hw11.py::TestImprovedHappyFruits::test_case_difference PASSED       [100%]

>>> pytest tests/hw11 -k TestImprovedUnhappyFruits -v
tests/hw11/test_hw11.py::TestImprovedUnhappyFruits::test_empty_string PASSED        [ 25%]
tests/hw11/test_hw11.py::TestImprovedUnhappyFruits::test_leading_space PASSED       [ 50%]
tests/hw11/test_hw11.py::TestImprovedUnhappyFruits::test_trailing_space PASSED      [ 75%]
tests/hw11/test_hw11.py::TestImprovedUnhappyFruits::test_non_matching_string PASSED [100%]

>>> pytest tests/hw11 -k TestImprovedErrors -v
tests/hw11/test_hw11.py::TestImprovedErrors::test_not_a_string_int PASSED           [ 16%]
tests/hw11/test_hw11.py::TestImprovedErrors::test_not_a_string_list PASSED          [ 33%]
tests/hw11/test_hw11.py::TestImprovedErrors::test_not_a_string_dict PASSED          [ 50%]
tests/hw11/test_hw11.py::TestImprovedErrors::test_not_a_string_bool PASSED          [ 66%]
tests/hw11/test_hw11.py::TestImprovedErrors::test_no_arg PASSED                     [ 83%]
tests/hw11/test_hw11.py::TestImprovedErrors::test_multiple_args PASSED              [100%]
"""


class TestImprovedHappyFruits(object):

    def test_banana(self):
        assert get_formal_name_improved('banana') == 'Musa acuminata'

    def test_peach(self):
        assert get_formal_name_improved('peach') == 'Prunus persica'

    def test_lemon(self):
        assert get_formal_name_improved('lemon') == 'Citrus limon'

    def test_case_difference(self):
        assert get_formal_name_improved('Peach') == 'Prunus persica'


class TestImprovedUnhappyFruits(object):

    def test_empty_string(self):
        with pytest.raises(KeyError):
            assert get_formal_name_improved('') == 'Musa acuminata'

    def test_leading_space(self):
        with pytest.raises(KeyError):
            assert get_formal_name_improved(' banana') == 'Musa acuminata'

    def test_trailing_space(self):
        with pytest.raises(KeyError):
            assert get_formal_name_improved('banana ') == 'Musa acuminata'

    def test_non_matching_string(self):
        with pytest.raises(KeyError):
            assert get_formal_name_improved('ananab') == 'Musa acuminata'


class TestImprovedErrors(object):

    def test_not_a_string_int(self):
        with pytest.raises(KeyError):
            assert get_formal_name_improved(56) == 'Musa acuminata'

    def test_not_a_string_list(self):
        with pytest.raises(KeyError):
            assert get_formal_name_improved(['banana']) == 'Musa acuminata'

    def test_not_a_string_dict(self):
        with pytest.raises(KeyError):
            assert get_formal_name_improved({1: 'banana'}) == 'Musa acuminata'

    def test_not_a_string_bool(self):
        with pytest.raises(KeyError):
            assert get_formal_name_improved(True) == 'Musa acuminata'

    def test_no_arg(self):
        # no args is not allowed
        with pytest.raises(TypeError):
            assert get_formal_name_improved() == 'Musa acuminata'

    def test_multiple_args(self):
        # 2 args is not allowed
        with pytest.raises(TypeError):
            assert get_formal_name_improved('banana', 'plum') == 'Musa acuminata'
