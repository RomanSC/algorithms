""" norecurse.py | UTF-8 | Mon, Jan 23, 2017 | Roman S. Collins

    An implementation of calculating Fibonacci of n using various functions,
    while plotting their efficiency in miliseconds.

    Problem:
    http://cs.marlboro.edu/courses/spring2017/algorithms/special/assignments

    Find the ratio of consecutive Fibonnaci numbers for large n.

    Bonus: Make a plot of n vs Fib[n], fit to a curve of the form, and discuss.

    Dependencies:
    - python matplotlib library
    - python sympy library

    TODO:
    - Plot using matplotlib
    - Create many Fibonacci of n functions

    Sources:

    - 5 Ways of Fibonacci in Python:
        https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/

    - Five Ways to Calculate Fibonacci Numbers with Python Code
        http://sahandsaba.com/five-ways-to-calculate-fibonacci-numbers-with-python-code.html

"""
import time, math, sys
import matplotlib.pyplot as pyplot
sys.setrecursionlimit(18000)

class Fibby():
    #TODO
    # Plot function!!!
    def plot(self):
        pass

    # Source: Python tutoring with Dylan
    # This method uses "tail recursion"
    # http://pastebin.com/89dxMK2L
    def fib1(self, n):
        prev = {}
        # Because if n is equal to 0 or 1, Fibonacci of n
        # will equal 0 or 1 respectively
        if (n == 0) or (n == 1):

            return n
        # Tail recursion
        # If n has already been calculated don't do it
        # over again
        if n in prev:

            return prev[n]

        prev[n] = self.fib1(n-1) + self.fib1(n-2)

        return prev[n]

    # Source: A YouTube video
    # https://www.youtube.com/watch?v=CKPciT2ROL8
    # https://dl.dropboxusercontent.com/u/4904309/fib-spiral.py
    # This method is a modified version of the source above
    # and is very "recursive"
    def fib2(self, n):
        # let n be number of iterations
        # Gold().fibby(10) returns 55:
        # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
        ns = []

        n1, n2 = 0, 1
        if (n == 0) or (n == 1):

            return n

        else:
            for iteration in range(n - 1):
                n = n1 + n2
                n1 = n2
                n2 = n
                ns.append(n)

            return n

    # Source: 5 Ways of Fibonacci in Python
    # Example 1: Using looping technique
    def fib3(self, n):
        a, b = 1, 1

        for i in range(n - 1):
            a, b = b, a + b

        return a

    # Source: 5 Ways of Fibonacci in Python
    # Example 2: Using recursion
    # Nearly identical to my fib2()
    def fib4(self, n):
        if (n == 1) or (n == 2):

            return n

        return self.fib4(n - 1) + self.fib4(n - 2)

    # Source: 5 Ways of Fibonacci in Python
    # Example 3: Using generators
#    def fib5(self):
#        a, b = 0, 1
#        global a, b
#
#        while True:
#            a, b = b, a + b
#
#            yield a
#
#        f = fibI()
#        f.next()
#        f.next()
#        f.next()
#        f.next()

# Hmmm... Memoization.

#    # Source: 5 Ways of Fibonacci in Python
#    # Example 4: Using Memoization
#    def fib6(self, fn, arg):
#        memo = {}
#
#        if arg not in memo:
#            memo[arg] = fn(arg)
#
#            return memo[arg]
#
#class Memoize:
# def __init__(self, fn):
#  self.fn = fn
#  self.memo = {}
# def __call__(self, arg):
#  if arg not in self.memo:
#   self.memo[arg] = self.fn(arg)
#   return self.memo[arg]
#
#@Memoize
#def fib(n):
# a,b = 1,1
# for i in range(n-1):
#  a,b = b,a+b
# return a
#print fib(5)

def main():
    #n = int(input('Calculate Fibonacci of?: '))
    #n_plus = (int(n) + 1)

    fibby = Fibby()

    #print(fibby.fib1(n) / fibby.fib1(n + 1))

    #print(fibby.fib2(n) / fibby.fib2(n + 1))

    #print(fibby.fib3(n) / fibby.fib3(n + 1))

    #print(fibby.fib5(n) / fibby.fib5(n + 1))

    #print(fibby.fib6(n) / fibby.fib6(n + 1))
    #fibm = memoize(fib,5)
    #print fibm

    # fib1
    fib1_results = []
    fib1_times = []

    # fib2
    fib2_results = []
    fib2_times = []

    # fib3
    fib3_results = []
    fib3_times = []

    # fib4
    fib4_results = []
    fib4_times = []


    fib_of = 6
    for n in range(fib_of):
        # Make many veriables to ensure no false positive
        fib1_n, fib2_n, fib3_n, fib4_n = n, n, n, n

        # fib1
        start_time = time.time()

        fibby.fib1(fib1_n)

        end_time = time.time()

        fib1_results.append(fib1_n)
        fib1_times.append(end_time - start_time)

        pyplot.plot(fib1_results, fib1_times)


        # fib2
        start_time = time.time()

        fibby.fib2(fib2_n)

        end_time = time.time()

        fib2_results.append(fib2_n)
        fib2_times.append(end_time - start_time)

        pyplot.plot(fib2_results, fib2_times)

        # fib3
        start_time = time.time()

        fibby.fib3(fib3_n)

        end_time = time.time()

        fib3_results.append(fib3_n)
        fib3_times.append(end_time - start_time)

        pyplot.plot(fib3_results, fib3_times)

        # fib4
        #start_time = time.time()

        #fibby.fib4(fib4_n)

        #end_time = time.time()

        #fib4_results.append(fib4_n)
        #fib4_times.append(end_time - start_time)

        #pyplot.plot(fib4_results, fib4_times)


    pyplot.xlabel('n')
    pyplot.ylabel('time')
    pyplot.title('The Ways of Fibonacci: ')
    pyplot.grid(True)
    #pyplot.savefig("test.png")
    pyplot.show()

if __name__ == '__main__':
    main()
