import pytest
from math import *
from heap_a import Heap

def test_heap_make_2():
    heap = Heap(2, [1,2,3,4,5,6,7])
    assert heap.value == [7,4,6,1,3,2,5]

def test_heap_make_3():
    heap = Heap(3, [1,2,3,4,5,6,7])
    assert heap.value == [7, 6, 2, 3, 1, 4, 5]

def test_heap_make_4():
    heap = Heap(4, [1,2,3,4,5,6,7])
    assert heap.value == [7, 6, 2, 3, 4, 1, 5]

def test_heap_push_2():
    heap = Heap(2, [])
    heap.push(3)
    heap.push(7)
    heap.push(1)
    heap.push(9)
    heap.push(6)
    heap.push(2)
    print(heap)
    assert heap.value == [9, 7, 2, 3, 6, 1]

def test_heap_push_3():
    heap = Heap(3, [])
    heap.push(3)
    heap.push(7)
    heap.push(1)
    heap.push(9)
    heap.push(6)
    heap.push(2)
    print(heap)
    assert heap.value == [9, 6, 1, 7, 3, 2]

def test_heap_push_4():
    heap = Heap(4, [])
    heap.push(3)
    heap.push(7)
    heap.push(1)
    heap.push(9)
    heap.push(6)
    heap.push(2)
    print(heap)
    assert heap.value == [9, 3, 1, 7, 6, 2]

def test_heap_pop_2():
    heap = Heap(2, [7, 6, 2, 3, 4, 1, 5])
    heap.pop()
    assert heap.value == [6, 4, 5, 3, 2, 1]

def test_heap_pop_3():
    heap = Heap(3, [7, 6, 2, 3, 4, 1, 5, 8, 6])
    heap.pop()
    heap.pop()
    heap.pop()
    assert heap.value == [6, 5, 2, 3, 4, 1]

def test_heap_pop_4():
    heap = Heap(4, [7, 6, 2, 3, 4, 1, 5, 8, 6])
    heap.pop()
    heap.pop()
    assert heap.value == [6, 6, 2, 3, 4, 1, 5]
