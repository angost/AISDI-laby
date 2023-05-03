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
        print(int(i))
        words = text.split()[:int(i)]
        start = time.process_time()
        for word in words:
            measure_type(word, text)
        stop = time.process_time()
        times.append(stop-start)
        print(stop-start)
    return times

def make_plot(text, measure_type):
    fig, ax = plt.subplots()
    measure_type, name = choose_method(measure_type)
    x = np.linspace(100, 1001, 10)
    y = measure(x, text, measure_type)

    ax.plot(x, y, linewidth=2.0)
    ax.set(xticks=np.linspace(100, 1000, 10))
    title = f"{name}"
    plt.title(title)
    plt.xlabel('Number of words')
    plt.ylabel('Time [s]')

    plt.savefig(f'{name}_plot.png')
    plt.show()


def compare_plot(text):
    fig, ax = plt.subplots()

    x = np.linspace(100, 1001, 10)
    naive = measure(x, text, find_naive)
    # naive = [8.421875, 16.71875, 25.59375, 45.875, 49.515625, 49.3125, 56.6875, 65.1875, 65.3125, 68.65625]
    kmp = measure(x, text, find_KMP)
    # kmp = [13.09375, 38.234375, 60.53125, 51.21875, 62.125, 73.546875, 103.890625, 98.234375, 109.1875, 124.875]
    kr = measure(x, text, find_KR)
    # kr = [89.96875, 154.859375, 246.0, 326.875, 438.96875, 524.953125, 612.921875, 695.859375, 777.421875, 868.875]

    ax.plot(x, naive, linewidth=2.0, label='NAIVE')
    ax.plot(x, kmp, linewidth=2.0, label='KMP')
    ax.plot(x, kr, linewidth=2.0, label='KR')

    plt.legend(loc="upper left")
    plt.xlabel('Number of elements')
    plt.ylabel('Time [s]')

    ax.set(xticks=np.linspace(100, 1000, 10))


    plt.savefig('find_pattern_comparison.png')
    plt.show()


def main():
    with open('pan-tadeusz.txt','r',encoding="utf-8") as file_handle:
        text = file_handle.read()
    make_plot(text, 3)
    # compare_plot(text)



if __name__ == "__main__":
    main()

