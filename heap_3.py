
#           9(0)
#     2(1)     5(2)     3(3)
# 1(4) 0(5) 0(6)  3(7) 4(8) 2(9)  1(10) 2(11) 3(12)


from math import *

def push_3(el, heap:list):
    heap.append(el)
    index = len(heap) - 1
    p_index = max((index-1)//3, 0)
    while heap[index] > heap[p_index]:
        heap[index], heap[p_index] = heap[p_index], heap[index]
        index = p_index
        p_index = max((index-1)//3, 0)
    return heap

def make_heap_3(list):
    heap = []
    for el in list:
        heap = push_3(el, heap)
    return heap

# def print_heap_3(heap:list):
#     n_of_levels = 0
#     n_of_elements = 0
#     while n_of_elements < len(heap):
#         n_of_elements += 3**n_of_levels
#         n_of_levels += 1
#     print(n_of_levels)
#     max_len = 3**(n_of_levels-1)
#     for i in range(n_of_levels):
#         level_start = (3**i)-1 # wymyslic
#         level_end = (3**i)-1 + 3**i # wymyslic
#         fill_level = []
#         if len(heap) <= level_end:
#             fill_level = [" " for j in range(level_end-len(heap)+1)]
#             level_end = len(heap)
#         level = heap[level_start:level_end] + fill_level
#         level = [str(num) for num in level]
#         print((" ".join(level)).center(max_len*2-1, " "))

list = [5,2,4,1,0,3,9,5,7,1]
list = [1 for i in range(40)]
print(list)
heap = make_heap_3(list)
print(heap)
print_heap_3(heap)