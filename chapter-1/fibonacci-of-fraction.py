""" fibonacci-of-fraction.py | UTF-8 | Thu, Jan 26, 2017 | Roman S. Collins

    Using the fractions class and generating fibonacci sequence with it.

"""
#from fraction import Fraction

class Fibby:
    def fib(self, n):
        prev = [0, 1]
        #if (n == 0) or (n ==1):
        #    return prev[n]
        if n not in prev:
            return prev[n]

def main():

    print(Fibby().fib(10))

if __name__ == '__main__':
    main()
