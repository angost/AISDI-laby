
from math import *

class Heap():

    def __init__(self, degree, list):
        self.degree = degree
        self.value = []
        for el in list:
            self.push(el)

    def push(self, el):
        heap = self.value

        heap.append(el)
        index = len(heap) - 1
        p_index = max((index-1)//self.degree, 0)
        while heap[index] > heap[p_index]:
            heap[index], heap[p_index] = heap[p_index], heap[index]
            index = p_index
            p_index = max((index-1)//self.degree, 0)

        self.value = heap
        return self.value

    def pop(self):
        heap = self.value

        if heap == []:
            return self.value

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

        self.value = heap
        return self.value

    def print(self):
        heap = self.value

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



list = [5,2,4,1,0,3]
list = [5,2,4,1,0,3,9,5,7,1]
heap = Heap(2, list)
print(heap.value)
heap.print()
heap.pop()
heap.print()