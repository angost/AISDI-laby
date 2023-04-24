import random
from heap_a import Heap
import time
import matplotlib.pyplot as plt
import numpy as np

def choose_measure(number):
    if number == 1:
        return measure_create, 'Create'
    if number == 2:
        return measure_pop, 'Pop'
    assert ValueError('Selected invalid measure option.')

def measure_create(x, elements, n):
    times = []
    for i in x:
        start = time.process_time()
        Heap(n, elements[:i])
        stop = time.process_time()
        times.append(stop-start)
    return times

def measure_pop(x, elements, n):
    times = []
    for i in x:
        heap = Heap(n, elements)
        start = time.process_time()
        for j in range(i):
            heap.pop()
        stop = time.process_time()
        times.append(stop-start)
    return times

def make_plot(heap_elements, n, measure_type):
    fig, ax = plt.subplots()
    measure, name = choose_measure(measure_type)
    x = np.linspace(1000, 10001, 10)
    y = measure(x, heap_elements, n)

    ax.plot(x, y, linewidth=2.0)
    ax.set(xticks=np.linspace(1000, 10000, 10))
    title = f"Heap: {name}"
    plt.title(title)
    plt.xlabel('Number of words')
    plt.ylabel('Time [s]')

    # plt.savefig(f'heap{n}_{name}.png')
    plt.show()


def compare_plot(heap_elements, measure_type):
    fig, ax = plt.subplots()
    measure, name = choose_measure(measure_type)

    x = np.linspace(1000, 10001, 10)
    two = measure(x, heap_elements, 2)
    three = measure(x, heap_elements, 3)
    four = measure(x, heap_elements, 4)

    ax.plot(x, two, linewidth=2.0, label=f'Heap_2: {name}')
    ax.plot(x, three, linewidth=2.0, label=f'Heap_3: {name}')
    ax.plot(x, four, linewidth=2.0, label=f'Heap_4: {name}')

    plt.legend(loc="upper left")
    plt.xlabel('Number of elements')
    plt.ylabel('Time [s]')

    ax.set(xticks=np.linspace(1000, 10000, 10))


    # plt.savefig(f'heap_{name}_comparison.png')
    plt.show()


def main():
    random_numbers = random.sample(range(0,300000), 100)
    make_plot(random_numbers, 2, 1)


if __name__ == "__main__":
    main()
