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
    if length == 1 or length == 0:
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


def quick_sort(list_to_sort):

    length = len(list_to_sort)
    if length == 1 or length == 0:
        return list_to_sort

    pivot = -1
    bigger_left = 0
    smaller_right = length - 2

    found_bigger_left = False
    found_smaller_right = False

    for loop_number in range(length - 1):
        # Od lewej
        for i in range(bigger_left, length - 1):
            if list_to_sort[i] > list_to_sort[pivot]:
                bigger_left = i
                found_bigger_left = True
                break
            # Jesli to jest ostatnie i i nie znaleziono LW -> pivot jest najwiekszy
            # if i == length-2:
            #     pass
        if not found_bigger_left:
            bigger_left = length-1
            break

        # Od prawej
        for i in range(0, smaller_right + 1):
            if list_to_sort[smaller_right - i] < list_to_sort[pivot]:
                smaller_right = smaller_right - i
                found_smaller_right = True
                break
            # Sprawdzamy 0 element listy i nie znaleziono PM -> pivot jest najmniejszy
            if i == length - 2:
                list_to_sort[0], list_to_sort[pivot] = list_to_sort[pivot], list_to_sort[0]
        if not found_smaller_right:
             bigger_left = 0
             break

        # lewy > prawy -> stop
        if bigger_left > smaller_right:
            list_to_sort[bigger_left], list_to_sort[pivot] = list_to_sort[pivot], list_to_sort[bigger_left]
            break

        #swap
        list_to_sort[bigger_left], list_to_sort[smaller_right] = list_to_sort[smaller_right], list_to_sort[bigger_left]

    left_sorted = quick_sort(list_to_sort[:bigger_left])
    right_sorted = quick_sort(list_to_sort[bigger_left + 1:])
    pivot = [list_to_sort[bigger_left]]
    return left_sorted + pivot + right_sorted
