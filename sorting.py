from math import ceil

def bubble_sort(list_to_sort):
    length = len(list_to_sort)
    for i in range(length-1):
        for j in range(length-i-1):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    return list_to_sort


def selection_sort(list_to_sort):
    length = len(list_to_sort)
    for i in range(length-1):
        min_el = (list_to_sort[i], i)
        for j in range(i, length):
            if list_to_sort[j] < min_el[0]:
                min_el = (list_to_sort[j], j)
        list_to_sort[i], list_to_sort[min_el[1]] = list_to_sort[min_el[1]], list_to_sort[i]
    return list_to_sort


def merge_sort(list_to_sort):
    return divide(list_to_sort)

def divide(list_to_sort):
    length = len(list_to_sort)
    if length == 1:
        return list_to_sort
    middle = ceil(length/2)
    left = divide(list_to_sort[:middle])
    right = divide(list_to_sort[middle:])
    return merge(left, right)

def merge(left, right):
    merged = []
    for i in range(len(left)):
        # TODO naprawic, jak j sie koncza
        for j in range(len(right)):
            if left[i] < right[j]:
                merged.append(left[i])
                break
            else:
                merged.append(right[j])
    merged += right[j:]
    return merged
    
def quick_sort(list_to_sort):
    return list_to_sort
