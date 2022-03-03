import pytest
import separate


def test_odds_evens():
    res = separate.separate_odd_even([3, 5, 6, 3, 4, 8, 9])
    assert res == [3, 5, 3, 9, 6, 4, 8]


def test_odds_only_returns_odds_only():
    res = separate.separate_odd_even([3, 5, 3, 9])
    assert res == [3, 5, 3, 9]


def test_even_only_returns_even_only():
    res = separate.separate_odd_even([2, 16, 8, 24])
    assert res == [2, 16, 8, 24]


def test_empty():
    res = separate.separate_odd_even([])
    assert res == []


def test_odds_evens_inplace():
    nums = [3, 5, 6, 3, 4, 8, 9]
    separate.separate_odd_even_in_place(nums)
    assert nums == [3, 5, 3, 9, 6, 4, 8]


def test_odds_only_returns_odds_only_inplace():
    nums = [3, 5, 3, 9]
    separate.separate_odd_even_in_place(nums)
    assert nums == [3, 5, 3, 9]


def test_even_only_returns_even_only_inplace():
    nums = [2, 16, 8, 24]
    separate.separate_odd_even_in_place(nums)
    assert nums == [2, 16, 8, 24]


def test_empty_inplace():
    nums = []
    res = separate.separate_odd_even_in_place(nums)
    assert nums == []
