"""
"""
import math
from matplotlib import pyplot
from executiontime import execution_time
from waysoffib import *

wof = WAYSOFFIB()

def main():
    pass

    n = 10

    pyplot.plot(wof.catalogued(n))
    pyplot.plot(wof.not_catalogued(n))
    pyplot.plot(wof.looping(n))

    pyplot.xlabel('')
    pyplot.ylabel('Processing time')
    pyplot.title('')
    pyplot.grid(False)
    pyplot.show()

if __name__=='__main__':
    main()
