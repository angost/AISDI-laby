
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

# Removing heap's root
def pop_3(heap):
    if heap == []:
        return heap
    heap[0] = heap[len(heap)-1]
    heap.pop()
    heap_end = len(heap)
    index = 0
    lc_index = 3 * index + 1
    mc_index = 3 * index + 2
    rc_index = 3 * index + 3

    el_on_wrong_position = True
    while el_on_wrong_position:
        if lc_index < heap_end and heap[index] < heap[lc_index]:
            heap[index], heap[lc_index] = heap[lc_index], heap[index]
            index = lc_index
            lc_index = 3 * index + 1
        elif mc_index < heap_end and heap[index] < heap[mc_index]:
            heap[index], heap[mc_index] = heap[mc_index], heap[index]
            index = mc_index
            mc_index = 3 * index + 2
        elif rc_index < heap_end and heap[index] < heap[rc_index]:
            heap[index], heap[rc_index] = heap[rc_index], heap[index]
            index = rc_index
            rc_index = 3 * index + 3
        else:
            el_on_wrong_position = False
    return heap

def make_heap_3(list):
    heap = []
    for el in list:
        heap = push_3(el, heap)
    return heap

def print_heap_3(heap:list):
    n_of_levels = 0
    n_of_elements = 0
    while n_of_elements < len(heap):
        n_of_elements += 3**n_of_levels
        n_of_levels += 1
    # print(n_of_levels)
    max_len = 3**(n_of_levels-1)
    level_start = 0
    for i in range(n_of_levels):
        level_end = level_start + 3**i
        fill_level = []
        if len(heap) <= level_end:
            fill_level = [" " for j in range(level_end-len(heap)+1)]
            level_end = len(heap)
        level = heap[level_start:level_end] + fill_level
        level = [str(num) for num in level]
        print((" ".join(level)).center(max_len*2-1, " "))
        level_start = level_end

list = [5,2,4,1,0,3,9,5,7,1]
# list = [1 for i in range(40)]
print(list)
heap = make_heap_3(list)
print(heap)
print_heap_3(heap)
pop_3(heap)
print_heap_3(heap)