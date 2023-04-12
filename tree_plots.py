import random
from BST_trees import make_tree
from AVL_trees import make_AVL_tree
import time
import matplotlib.pyplot as plt
import numpy as np

def choose_measure(number):
    if number == 1:
        return measure_make, 'Make'
    if number == 2:
        return measure_search, 'Search'
    if number == 3:
        return measure_delete, 'Remove'
    assert ValueError('Selected invalid measure option.')

def measure_make(tree_type, x, elements):
    times = []
    for i in x:
        start = time.process_time()
        tree_type(elements)
        stop = time.process_time()
        times.append(stop-start)
    return times

def measure_search(tree_type, x, elements):
    times = []
    for i in x:
        tree = tree_type(elements)
        start = time.process_time()
        for j in elements[:int(i)]:
            tree.search_in_tree(j)
        stop = time.process_time()
        times.append(stop-start)
    return times

def measure_delete(tree_type, x, elements):
    times = []
    for i in x:
        tree = tree_type(elements)
        start = time.process_time()
        for j in elements[1:(int(i)-1)]:
            tree.remove_from_tree(j)
        stop = time.process_time()
        times.append(stop-start)
    return times


def make_plot(tree_type, tree_elements, measure_type):
    fig, ax = plt.subplots()
    measure, name = choose_measure(measure_type)
    x = np.linspace(1000, 10001, 10)
    y = measure(tree_type, x, tree_elements)

    ax.plot(x, y, linewidth=2.0)
    ax.set(xticks=np.linspace(1000, 10000, 10))
    if tree_type.__name__ == 'make_tree':
        title = f"{name} BST Tree"
    else: title = f"{name} AVL Tree"
    plt.title(title)
    plt.xlabel('Number of words')
    plt.ylabel('Time [s]')

    # plt.savefig(f'{tree_type.__name__}.png')
    plt.show()


def compare_plot(tree_elements, measure_type):
    fig, ax = plt.subplots()
    measure, name = choose_measure(measure_type)

    x = np.linspace(1000, 10001, 10)
    bst = measure(make_tree, x, tree_elements)
    avl = measure(make_AVL_tree, x, tree_elements)

    ax.plot(x, bst, linewidth=2.0, label=f'{name} BST')
    ax.plot(x, avl, linewidth=2.0, label=f'{name} AVL')

    plt.legend(loc="upper left")
    plt.xlabel('Number of elements')
    plt.ylabel('Time [s]')

    ax.set(xticks=np.linspace(1000, 10000, 10))


    plt.savefig(f'{name}_comparison.png')
    plt.show()


def main():
    random_numbers = random.sample(range(0,300000), 10000)
    # make_plot(make_tree, random_numbers, 1)
    # make_plot(make_AVL_tree, random_numbers, 1)
    compare_plot(random_numbers, 1)
    # make_plot(make_tree, random_numbers, 2)
    # make_plot(make_AVL_tree, random_numbers, 2)
    compare_plot(random_numbers, 2)
    # make_plot(make_tree, random_numbers, 3)
    # make_plot(make_AVL_tree, random_numbers, 3)
    compare_plot(random_numbers, 3)


if __name__ == "__main__":
    main()
