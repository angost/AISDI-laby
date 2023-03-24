from sorting import bubble_sort, merge_sort, selection_sort, quick_sort
from matplotlib import pyplot as plt
import numpy as np
import time


def get_data(n):
    with open('pan-tadeusz.txt', 'r', encoding='utf-8') as file_handle:
        words = file_handle.read()
        words = words.split()
    words = words[:n]
    return words


def measure(sorting_function, x):
    times = []
    for i in x:
        words = get_data(int(i))
        start = time.process_time()
        sorting_function(words)
        stop = time.process_time()
        times.append(stop-start)
    return times


def make_plot(sorting_function):
    fig, ax = plt.subplots()

    x = np.linspace(1000, 10001, 10)
    y = measure(sorting_function, x)

    ax.plot(x, y, linewidth=2.0)
    ax.set(xticks=np.linspace(1000, 10000, 10))
    plt.title(f'{sorting_function.__name__}')
    plt.xlabel('Number of words')
    plt.ylabel('Time [s]')

    plt.savefig(f'{sorting_function.__name__}.png')
    # plt.show()


def compare_plot():
    fig, ax = plt.subplots()

    x = np.linspace(1000, 10001, 10)
    bubbley = measure(bubble_sort, x)
    mergey = measure(merge_sort, x)
    selectiony = measure(selection_sort, x)
    quicky = measure(quick_sort, x)

    ax.plot(x, bubbley, linewidth=2.0, label='bubble')
    ax.plot(x, mergey, linewidth=2.0, label='merge')
    ax.plot(x, selectiony, linewidth=2.0, label='selection')
    ax.plot(x, quicky, linewidth=2.0, label='quick')

    plt.legend(loc="upper left")
    plt.xlabel('Number of words')
    plt.ylabel('Time [s]')

    ax.set(xticks=np.linspace(1000, 10000, 10))


    plt.savefig('comparison.png')
    #plt.show()


def main():
    make_plot(bubble_sort)
    make_plot(selection_sort)
    make_plot(merge_sort)
    make_plot(quick_sort)
    compare_plot()


if __name__ == "__main__":
    main()
