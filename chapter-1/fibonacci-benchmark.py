""" fibonacci-benchmark.py | Fri, Jan 27, 2017 | Roman S. Collins

    Comparing calculation times of different fibonacci functions.

"""
import time, sys
import numpy as np

# Import the functions
from waysoffib import *

def main():
    n = 34
    tmany = 10

    wof = WAYSOFFIB()
    mof = Memoize(n)

    fibs = [wof.catalogued(n), wof.not_catalogued(n), wof.looping(n), wof.gen(n)]
    f_key = ['wof.catalogued(n)', 'wof.not_catalogued(n)', 'wof.looping(n)', 'wof.gen(n)']

    x = fibs[0]
    print('Calculating fibonacci of', n, '=', x, 'calculated', tmany, 'times.')

    benchmarks = {'wof.catalogued(n)': [],
               'wof.not_catalogued(n)': [],
               'wof.looping(n)': [],
               'wof.gen(n)': []}

    for ___ in range(tmany):
        for fib in range(len(fibs)):
            key = str(f_key[fib])
            #print(f_key[fib])

            start = time.time()
            calc = fibs[fib]
            end = time.time()

            benchmark = float(end - start)

            benchmarks[key].append(benchmark)

    #print(benchmarks)

    print('METHOD:                    AVERAGE TIME:')
    #for i in range(len(benchmarks)):
    #    print(':', str(benchmarks[i])[:-4])
    for i in range(len(fibs)):
        key = str(f_key[i])
        benchmarks[key] = np.mean(benchmarks[key])

    for i in range(len(fibs)):
        key = str(f_key[i])
        mstr = str(key + ': ')

        if key == str(f_key[0]):
            space = '      '
        elif key == str(f_key[1]):
            space = '  '
        elif key == str(f_key[2]):
            space = '         '
        elif key == str(f_key[3]):
            space = '             '
        #space = ' '
        print(mstr, space, str(benchmarks[key])[:-6])

if __name__ == '__main__':
    main()
