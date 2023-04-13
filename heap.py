
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
        if lc_index < heap_end and heap[index] < heap[lc_index]:
            heap[index], heap[lc_index] = heap[lc_index], heap[index]
            index = lc_index
            lc_index = 2 * index + 1
        elif rc_index < heap_end and heap[index] < heap[rc_index]:
            heap[index], heap[rc_index] = heap[rc_index], heap[index]
            index = rc_index
            rc_index = 2 * index + 2
        else:
            el_on_wrong_position = False
    return heap

def make_heap_2(list):
    heap = []
    for el in list:
        heap = push_2(el, heap)
    return heap

print("aaa")
heap = make_heap_2([5,2,4,1,0,3])

