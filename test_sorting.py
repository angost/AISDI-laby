import pytest
from sorting import bubble_sort, selection_sort, merge_sort, quick_sort


def test_bubble_sort():
    sort_list = [2, 10, 4, 2, 1, 2, 6, 8, 3]
    assert bubble_sort(sort_list) == sorted(sort_list)
    sort_list = [1,1,1,1]
    assert bubble_sort(sort_list) == sorted(sort_list)
    sort_list = [1,2,3,4]
    assert bubble_sort(sort_list) == sorted(sort_list)
    sort_list = [4,3,2,1]
    assert bubble_sort(sort_list) == sorted(sort_list)
    sort_list = [5, 4, 6]
    assert bubble_sort(sort_list) == sorted(sort_list)
    sort_list = [5,4,6,7]
    assert bubble_sort(sort_list) == sorted(sort_list)
    sort_list = [1]
    assert bubble_sort(sort_list) == sorted(sort_list)
    sort_list = []
    assert bubble_sort(sort_list) == sorted(sort_list)
    sort_list = [5,6]
    assert bubble_sort(sort_list) == sorted(sort_list)
    sort_list = [1,1,1,1]
    assert bubble_sort(sort_list) == sorted(sort_list)

def test_selection_sort():
    sort_list = [2, 10, 4, 2, 1, 2, 6, 8, 3]
    assert selection_sort(sort_list) == sorted(sort_list)
    sort_list = [1,1,1,1]
    assert selection_sort(sort_list) == sorted(sort_list)
    sort_list = [1,2,3,4]
    assert selection_sort(sort_list) == sorted(sort_list)
    sort_list = [4,3,2,1]
    assert selection_sort(sort_list) == sorted(sort_list)
    sort_list = [5, 4, 6]
    assert selection_sort(sort_list) == sorted(sort_list)
    sort_list = [5,4,6,7]
    assert selection_sort(sort_list) == sorted(sort_list)
    sort_list = [1]
    assert selection_sort(sort_list) == sorted(sort_list)
    sort_list = []
    assert selection_sort(sort_list) == sorted(sort_list)
    sort_list = [5,6]
    assert selection_sort(sort_list) == sorted(sort_list)
    sort_list = [1,1,1,1]
    assert selection_sort(sort_list) == sorted(sort_list)

def test_merge_sort():
    sort_list = [2, 10, 4, 2, 1, 2, 6, 8, 3]
    assert merge_sort(sort_list) == sorted(sort_list)
    sort_list = [1,1,1,1]
    assert merge_sort(sort_list) == sorted(sort_list)
    sort_list = [1,2,3,4]
    assert merge_sort(sort_list) == sorted(sort_list)
    sort_list = [4,3,2,1]
    assert merge_sort(sort_list) == sorted(sort_list)
    sort_list = [5, 4, 6]
    assert merge_sort(sort_list) == sorted(sort_list)
    sort_list = [5,4,6,7]
    assert merge_sort(sort_list) == sorted(sort_list)
    sort_list = [1]
    assert merge_sort(sort_list) == sorted(sort_list)
    sort_list = []
    assert merge_sort(sort_list) == sorted(sort_list)
    sort_list = [5,6]
    assert merge_sort(sort_list) == sorted(sort_list)
    sort_list = [1,1,1,1]
    assert merge_sort(sort_list) == sorted(sort_list)

def test_quick_sort():
    sort_list = [2, 10, 4, 2, 1, 2, 6, 8, 3]
    assert quick_sort(sort_list) == sorted(sort_list)
    sort_list = [1,1,1,1]
    assert quick_sort(sort_list) == sorted(sort_list)
    sort_list = [1,2,3,4]
    assert quick_sort(sort_list) == sorted(sort_list)
    sort_list = [4,3,2,1]
    assert quick_sort(sort_list) == sorted(sort_list)
    sort_list = [5, 4, 6]
    assert quick_sort(sort_list) == sorted(sort_list)
    sort_list = [5,4,6,7]
    assert quick_sort(sort_list) == sorted(sort_list)
    sort_list = [1]
    assert quick_sort(sort_list) == sorted(sort_list)
    sort_list = []
    assert quick_sort(sort_list) == sorted(sort_list)
    sort_list = [5,6]
    assert quick_sort(sort_list) == sorted(sort_list)
    sort_list = [1,1,1,1]
    assert quick_sort(sort_list) == sorted(sort_list)
