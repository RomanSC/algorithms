""" analysis.py | Tue, Mar, 28, 2017 | Roman S. Collins
"""
import math
from createlist import create
from funtime import timeme
from quicksort import quicksort
from mergesort import mergesort
from matplotlib import pyplot

def analysis(n, function):
    data = []

    for z in range(n):
        testlist = create(iterations=z, floor=1, ceiling=20, countby=2)

        av_extime = average_extime(testlist, function)
        data.append(av_extime)

        print(z)

    return data


def average_extime(testlist, function):
    extimes = []

    for i in range(100):
        function_returned, function_time = timeme(function)

        #print(function_time)

        if function_time > 0:
            extimes.append(function_time)

    print(len(extimes))

    average_extimes = sum(extimes) / len(extimes)

    return average_extimes

def main():
    testlist = [1]
    mfunction = mergesort
    qfunction = quicksort
    dfunction = sorted

    n = 1000

    mergesort_data = analysis(n, mfunction)
    quicksort_data = analysis(n, qfunction)
    default_data = analysis(n, dfunction)

    title = "Run-time Analysis:"
    label_y = "Average Time"
    label_x = "Size of lists"

    mergesort_plot = pyplot.plot(mergesort_data, label='Mergesort')
    quicksort_plot = pyplot.plot(quicksort_data, label='Quicksort')
    default_data = pyplot.plot(default_data, label='Default Sorted()')

    pyplot.legend(loc='best')
    pyplot.ylabel(label_y)
    pyplot.xlabel(label_x)
    pyplot.title(title)
    pyplot.grid(False)

    pyplot.show()

if __name__ == "__main__":
    main()
