"""
"""
import time

prev = {}

def fib(n):
    #prev = {}
    if (n == 0) or (n == 1):
        return float(n)
    if n in prev:
        return prev[n]

    prev[n] = fib(n-1) + fib(n-2)

    return float(prev[n])

def main():

    n = 997
    #fibslist = [fib(i) for i in range(1, (n + 1))]

    #print(fibslist)

    print(time.time())
    print(fib(n)/fib(n + 1))
    print(time.time())

    print(time.time())
    print(fib(n + 1)/fib(n))
    print(time.time())

if __name__ == '__main__':
    main()
