import pytest
from closest_to_zero import closest_to_zero


def test_wrong_input_string():
    assert closest_to_zero('toto') == 0


def test_wrong_input_empty_list():
    assert closest_to_zero([]) == 0


def test_wrong_input_nested_list():
    assert closest_to_zero([[2, 3], [-1]]) == 0


def test_wrong_input_string_list():
    assert closest_to_zero(list('abc')) == 0


def test_correct_input_singleton():
    assert closest_to_zero(set([2])) == 2


def test_correct_input_single_minimum():
    assert closest_to_zero((5, 4, -9, 6, -10, -1, 8)) == -1


def test_correct_input_positive_value():
    assert closest_to_zero([5, 4, -9, 6, -10, -1, 8, 1]) == 1


def test_correct_input_with_zero():
    assert closest_to_zero([2, 0]) == 0
