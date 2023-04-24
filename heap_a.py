
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

        el_on_wrong_position = True
        while el_on_wrong_position:
            children = []

            # Checking which children exist
            for child_number in range(1, self.degree + 1):
                c_index = self.degree * index + child_number
                if c_index < heap_end:
                    children.append(c_index)
                else:
                    break

            # Checking if swap is required
            if not children:
                el_on_wrong_position = False
            else:
                greater_c_index = max(children, key= lambda i : heap[i])
                if heap[greater_c_index] > heap[index]:
                    heap[index], heap[greater_c_index] = heap[greater_c_index], heap[index]
                    index = greater_c_index
                else:
                    el_on_wrong_position = False

        self.value = heap
        return self.value

    def __str__(self):
        heap = self.value
        txt_heap = ''

        n_of_levels = 0
        n_of_elements = 0
        while n_of_elements < len(heap):
            n_of_elements += self.degree**n_of_levels
            n_of_levels += 1
        max_len = self.degree**(n_of_levels-1)

        level_start = 0
        for i in range(n_of_levels):
            level_end = level_start + self.degree**i
            fill_level = []
            if len(heap) <= level_end:
                fill_level = [" " for j in range(level_end-len(heap)+1)]
                level_end = len(heap)
            level = heap[level_start:level_end] + fill_level
            level = [str(num) for num in level]
            txt_heap += (" ".join(level)).center(max_len*2-1, " ") + '\n'
            level_start = level_end
        return txt_heap

# list = [5,2,4,1,0,3]
list = [5,2,4,0,1,3,9,5,7,1,9,0,31,5,12,10,5,8,9,3,45,7,9,3,6,3,7,9,235,73,42,2,34,7,9,0,0,0,0,1,1,13,6,7]
heap = Heap(4, list)
print(heap.value)
print(heap)
heap.pop()
print(heap)
