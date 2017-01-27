""" fibonacci-plot.py | UTF-8 | Thu, Jan 26, 2017 | Roman S. Collins

    Plotting various fibonacci functions in Python using the
    matplotlib library.

"""
import time, math, sys
import matplotlib.pyplot as pyplot

# Import fibonacci functions:
from waysoffib import *

class Plot:
    # Create proportional list of colors for pyplot
    def n_colors(self, n):
        colors = ['r', 'b', 'g', 'c', 'm', 'y']
        n_colors = []

        for i in range(n):
            # if n == 8, then 8 % 6 = 2
            # with a list of 6 colors
            # with 8 needed
            # the remainder of colors
            # need are calculated
            # providing those extra
            calc = int(i % len(colors))
            n_colors.append(colors[calc])

        return n_colors

    # Draw the plot
    def plot_me(self, title):
        pyplot.xlabel('F(n) = F(n - 1) + F(n - 2)')
        pyplot.ylabel('Processing time')
        pyplot.title(title)
        pyplot.grid(False)
        #pyplot.savefig("graph.png")
        pyplot.show()

# Main program
def main():
    n = 20
    # w will be an int representing
    # the total amount of fibonacci
    # functions tested here
    p = Plot()
    # Fibonacci functions
    # initialize
    waysoffib = WAYSOFFIB()
    memsoffib = Memoize(n)

    c_result = []
    c_times = []
    for x in range(n):
        start = time.time()

        waysoffib.catalogued(x)

        end = time.time()

        c_result.append(n)
        c_times.append([end - start])

    pyplot.plot(c_result, c_times, 'r-')
    #print(c_result, c_times)

    nc_result = []
    nc_times = []
    for x in range(n):
        start = time.time()

        waysoffib.not_catalogued(x)

        end = time.time()

        nc_result.append(n)
        nc_times.append([end - start])

    pyplot.plot(nc_result, nc_times, 'b-')
    #print(nc_result, nc_times)

    lp_result = []
    lp_times = []
    for x in range(n):
        start = time.time()

        waysoffib.looping(x)

        end = time.time()

        lp_result.append(n)
        lp_times.append([end - start])

    pyplot.plot(lp_result, lp_times, 'g-')
    #print(lp_result, lp_times)

    gn_result = []
    gn_times = []
    for x in range(n):
        start = time.time()

        waysoffib.gen(x)

        end = time.time()

        gn_result.append(n)
        gn_times.append([end - start])

    pyplot.plot(gn_result, gn_times, 'm-')
    #print(gn_result, gn_times)


    p.plot_me('The Ways of Fibonacci: ')
    """
    which_fib = [waysoffib.catalogued(n), waysoffib.not_catalogued(n), waysoffib.looping(n), waysoffib.gen(n)]

    #for x in range(len(which_fib)):
    #    calculations.append([])
    for i in range(len(which_fib)):
        #calculations[i][i] = which_fib[i]
        start = time.time()
        run = which_fib[i]
        end = time.time()

        calculations.append([run])
        benchmarks.append([start-end])

    colors = p.n_colors(len(which_fib))
    for x in range(len(calculations)):
        line = colors[i] + '-'
        pyplot.plot(calculations[x], benchmarks[x], line)

    print(calculations)
    print(benchmarks)

    p.plot_me('The Ways of Fibonacci: ')
    """

    """
    # Example data
    apllist = [0, 1, 2, 3, 4]
    bpllist = [2, 3, 4, 5, 6]
    cpllist = [4, 5, 6, 7, 8]
    dpllist = [6, 7, 8, 9, 10]
    epllist = [8, 9, 10, 11, 12]
    fpllist = [10, 11, 12, 13, 14, 15]
    # List of lists, each list provided by a fibonacci function
    # to iterate over
    which_fib = [apllist, bpllist, cpllist, dpllist, dpllist, epllist, fpllist]

    fibs_len = len(which_fib)
    colors = p.n_colors(fibs_len)

    for w in range(len(which_fib)):
        line = colors[w] + '-'
        pyplot.plot(which_fib[w], line)

    p.plot_me('The Ways of Fibonacci: ')
    """

    """
    print(waysoffib.catalogued(n))
    print(waysoffib.not_catalogued(n))
    print(waysoffib.looping(n))
    print(waysoffib.gen(n))
    """

if __name__ == '__main__':
    main()
