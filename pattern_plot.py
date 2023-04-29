from pattern import find_naive, find_KMP, find_KR
import time
import matplotlib.pyplot as plt
import numpy as np

def choose_method(number):
    if number == 1:
        return find_naive, 'Naive'
    if number == 2:
        return find_KMP, 'KMP'
    if number == 3:
        return find_KR, 'KR'
    assert ValueError('Selected invalid method option.')

def measure(x, text, measure_type):
    times = []
    for i in x:
        words = text.split()[:i]
        start = time.process_time()
        for word in words:
            measure_type(word, text)
        stop = time.process_time()
        times.append(stop-start)
    return times

def make_plot(text, measure_type):
    fig, ax = plt.subplots()
    measure_type, name = choose_method(measure_type)
    x = np.linspace(100, 1001, 10)
    y = measure(x, text, measure_type)

    ax.plot(x, y, linewidth=2.0)
    ax.set(xticks=np.linspace(100, 1000, 10))
    title = f"Heap: {name}"
    plt.title(title)
    plt.xlabel('Number of words')
    plt.ylabel('Time [s]')

    # plt.savefig(f'{name}_plot.png')
    plt.show()


def compare_plot(text):
    fig, ax = plt.subplots()

    x = np.linspace(100, 1001, 10)
    naive = measure(x, text, find_naive)
    kmp = measure(x, text, find_KMP)
    kr = measure(x, text, find_KR)

    ax.plot(x, naive, linewidth=2.0, label='NAIVE')
    ax.plot(x, kmp, linewidth=2.0, label='KMP')
    ax.plot(x, kr, linewidth=2.0, label='KR')

    plt.legend(loc="upper left")
    plt.xlabel('Number of elements')
    plt.ylabel('Time [s]')

    ax.set(xticks=np.linspace(100, 1000, 10))


    # plt.savefig('find_pattern_comparison.png')
    plt.show()


def main():
    with open('pan-tadeusz.txt','r') as file_handle:
        text = file_handle.read()
    make_plot(text, 1)



if __name__ == "__main__":
    main()

