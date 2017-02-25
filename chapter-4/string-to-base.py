""" base-convert.py | Sun, Feb 19, 2017 | Roman S. Collins

    Not my code. From Problem Solving with Data Structures and Algorithms.

    This code utilizes recursion to convert strings of numbers into their,
    equivalent base. Such as base 2 for binary or 16

    It cannot do strings or decimals.

"""

def convert(n, base):
    legalhex = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if n < base:
        return legalhex[n]

    else:
      return convert((n // base), base) + legalhex[n % base]

def main():
    print(convert(9000, 2))

if __name__ == '__main__':
    main()


