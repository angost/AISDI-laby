import pytest
from BST_trees import BST, make_tree, CannotRemoveRootError
from AVL_trees import AVL, make_AVL_tree

def test_bst_make_tree_one_el():
    bst = make_tree([5])
    assert bst.value == 5
    assert bst.left is None
    assert bst.right is None

def test_bst_make_tree_multiple_el():
    lst = [5, 2, 8, 1, 3, 7, 9]
    bst = make_tree(lst)
    assert bst.value == 5
    assert bst.left.value == 2
    assert bst.right.value == 8
    assert bst.left.left.value == 1
    assert bst.left.right.value == 3
    assert bst.right.left.value == 7
    assert bst.right.right.value == 9

def test_bst_find_min():
    bst = make_tree([3,8,1,4,0,9])
    assert bst.find_min_element() == bst.search_in_tree(0)

    bst = make_tree([3,8,1,4,0,9])
    assert bst.search_in_tree(8).find_min_element() == bst.search_in_tree(4)

    bst = make_tree([4,3,2,1])
    assert bst.find_min_element() == bst.search_in_tree(1)

    bst = make_tree([1,2,3,4])
    assert bst.find_min_element() == bst.search_in_tree(1)

    bst = make_tree([4,1,3,2])
    assert bst.find_min_element() == bst.search_in_tree(1)

    bst = make_tree([4])
    assert bst.find_min_element() == bst.search_in_tree(4)

def test_bts_CannotRemoveRootError():
    bst = BST(1, None)

    with pytest.raises(CannotRemoveRootError):
        bst.remove_from_tree(1)

def test_bst_insert():
    bst = make_tree([5, 3, 7, 2, 4, 6, 8])

    assert bst.value == 5
    assert bst.left.value == 3
    assert bst.right.value == 7
    assert bst.left.left.value == 2
    assert bst.left.right.value == 4
    assert bst.right.left.value == 6
    assert bst.right.right.value == 8

def test_bst_remove_from_tree():
    bst = make_tree([5, 3, 7, 2, 4, 6, 8])

    bst.remove_from_tree(3)
    assert bst.left.value == 4
    assert bst.left.left.value == 2

    bst.remove_from_tree(7)
    assert bst.right.value == 8
    assert bst.right.left.value == 6

    bst.remove_from_tree(5)
    assert bst.value == 6
    assert bst.left.value == 4
    assert bst.right.value == 8
    assert bst.left.left.value == 2

def test_make_AVL_tree_one_el():
    avl = make_AVL_tree([42])
    assert avl.value == 42
    assert avl.left is None
    assert avl.right is None

def test_make_AVL_tree_multiple_el():
    avl = make_AVL_tree([5, 3, 7, 2, 4, 6, 8])
    assert avl.value == 5
    assert avl.left.value == 3
    assert avl.right.value == 7
    assert avl.left.left.value == 2
    assert avl.left.right.value == 4
    assert avl.right.left.value == 6
    assert avl.right.right.value == 8

def test_avl_find_min():
    avl = make_tree([3,8,1,4,0,9])
    assert avl.find_min_element() == avl.search_in_tree(0)

    avl = make_tree([3,8,1,4,0,9])
    assert avl.search_in_tree(8).find_min_element() == avl.search_in_tree(4)

    avl = make_tree([4,3,2,1])
    assert avl.find_min_element() == avl.search_in_tree(1)

    avl = make_tree([1,2,3,4])
    assert avl.find_min_element() == avl.search_in_tree(1)

    avl = make_tree([4,1,3,2])
    assert avl.find_min_element() == avl.search_in_tree(1)

    avl = make_tree([4])
    assert avl.find_min_element() == avl.search_in_tree(4)

def test_avl_CannotRemoveRootError():
    avl = AVL(1, None)

    with pytest.raises(CannotRemoveRootError):
        avl.remove_from_tree(1)

def test_avl_insert():
    avl = make_AVL_tree([3,7,5,4,2,8,9,1,0])

    assert avl.value == 5
    assert avl.left.value == 3
    assert avl.right.value == 8
    assert avl.left.left.value == 1
    assert avl.left.right.value == 4
    assert avl.right.left.value == 7
    assert avl.right.right.value == 9
    assert avl.left.left.left.value == 0
    assert avl.left.left.right.value == 2

def test_avl_remove_from_tree():
    avl = make_tree([3,7,5,4,2,8,9,1,0])

    avl.remove_from_tree(5)
    avl.show_tree(1,0,0)
    assert avl.value == 3
    assert avl.right.value == 7
    assert avl.right.left.value == 4
    assert avl.left.value == 2
    assert avl.left.left.value == 1

    avl.remove_from_tree(7)
    assert avl.right.value == 8
    assert avl.right.left.value == 4

    avl.remove_from_tree(2)
    assert avl.left.value == 1
    assert avl.left.left.value == 0
    assert avl.left.right is None