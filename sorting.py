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
    # nad ktorym j-tem sie teraz zastanawiamy
    j_pointer = 0
    for i in range(len(left)):
        # nie przegladamy j-tow ktore zostaly juz wykorzystane
        for j in range(j_pointer, len(right)):
            if left[i] < right[j]:
                merged.append(left[i])
                break
            else:
                merged.append(right[j])
                j_pointer = j + 1
        # tutaj ladujemy albo po breaku albo gdy j sie skonczyly
        if j_pointer == len(right):
            # j-ty sie skonczyly -> wrzucamy pozostala liste i
            merged += left[i:]
            break
    # i sie skonczyly -> wrzucamy pozostala liste j
    merged += right[j_pointer:]
    return merged

def merge_no_comments(left, right):
    merged = []
    j_pointer = 0
    for i in range(len(left)):
        for j in range(j_pointer, len(right)):
            if left[i] < right[j]:
                merged.append(left[i])
                break
            else:
                merged.append(right[j])
                j_pointer = j + 1
        if j_pointer == len(right):
            merged += left[i:]
            break
    merged += right[j_pointer:]
    return merged

# 2 10 11   4
'''
00 -> 2
10 -> 4
1- -> [i:]
2
'''

# 0 2 4    1 3 5
'''
00 -> 0
10 -> 1
11 -> 2
21 -> 3
22 -> 4
- -> [j_pointer:]
'''
# 1 5 6    2 3 4
'''
00 -> 1
10 -> 2
11 -> 3
12 -> 4
1- -> [i:]
'''

def quick_sort(list_to_sort):
    return list_to_sort
