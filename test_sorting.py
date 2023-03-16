import pytest
from sorting import bubble_sort, selection_sort, merge_sort

def test_bubble_sort():
    sort_list = [2, 10, 4, 2, 1, 2, 6, 8, 3]
    assert bubble_sort(sort_list) == [1, 2, 2, 2, 3, 4, 6, 8, 10]

def test_selection_sort():
    sort_list = [2, 10, 4, 2, 1, 2, 6, 8, 3]
    assert selection_sort(sort_list) == [1, 2, 2, 2, 3, 4, 6, 8, 10]

def test_merge_sort():
    sort_list = [2, 10, 4, 2, 1, 2, 6, 8, 3]
    assert merge_sort(sort_list) == [1, 2, 2, 2, 3, 4, 6, 8, 10]
