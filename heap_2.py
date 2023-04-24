
# [3820274]
# ---->
# [8734202]

#  ^ ________^
#  /         \
# |  -     -  |
# |     ⌔     |
# |      ⌒    |
#  \_________/
#     ↑↑↑
#     KRET
from math import *

def push_2(el, heap:list):
    heap.append(el)
    index = len(heap) - 1
    p_index = max((index-1)//2, 0)
    while heap[index] > heap[p_index]:
        heap[index], heap[p_index] = heap[p_index], heap[index]
        index = p_index
        p_index = max((index-1)//2, 0)
    return heap


# Removing heap's root
def pop_2(heap):
    if heap == []:
        return heap
    heap[0] = heap[len(heap)-1]
    heap.pop()
    heap_end = len(heap)
    index = 0
    lc_index = 2 * index + 1
    rc_index = 2 * index + 2

    el_on_wrong_position = True
    while el_on_wrong_position:
        children = []
        # Checking if l,r child exists
        if lc_index < heap_end:
            children.append(lc_index)
        if rc_index < heap_end:
            children.append(rc_index)

        # Checking if swap is required
        if not children:
            el_on_wrong_position = False
        else:
            greater_c_index = max(children, key= lambda i : heap[i])
            heap[index], heap[greater_c_index] = heap[greater_c_index], heap[index]
            index = greater_c_index
            lc_index = 2 * index + 1
            rc_index = 2 * index + 2

    return heap

def make_heap_2(list):
    heap = []
    for el in list:
        heap = push_2(el, heap)
    return heap

def print_heap_2(heap:list):
    n_of_levels = ceil(log(len(heap)+1, 2))
    max_len = 2**(n_of_levels-1)
    for i in range(n_of_levels):
        level_start = (2**i)-1
        level_end = (2**(i+1)-1)
        fill_level = []
        if len(heap) <= level_end:
            fill_level = [" " for j in range(level_end-len(heap)+1)]
            level_end = len(heap)
        level = heap[level_start:level_end] + fill_level
        level = [str(num) for num in level]
        print((" ".join(level)).center(max_len*2-1, " "))
    # 0:1
    # 1:3
    # 3:7
    #len=7
    #7-7+1
    #len=6 7-6+1
    #
# print("aaa")
# # heap = make_heap_2([5,2,4,1,0,3])
# heap = make_heap_2([5,2,4,1,0,3,9,5,7,1])
# print(heap)
# # print_heap_2(heap)
# # pop_2(heap)
# # print_heap_2(heap)

