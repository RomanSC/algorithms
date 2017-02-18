""" turtlecolors.py | Fri, Feb 17, 2017 | Roman S. Collins

    A random color generator for python turtle.

"""
import random

def randcolor():
    nums = [float('%.2f' % (0.01 * i)) for i in range(1, (100 + 1))]
    color = []

    for i in range(3):
        color.append(random.choice(nums))

    return tuple(color)

def randred():
    nums = [float('%.2f' % (0.01 * i)) for i in range(1, (100 + 1))]
    color = []

    color.append(random.choice(nums))
    color.append(0.0)
    color.append(0.0)

    return tuple(color)


def randgreen():
    nums = [float('%.2f' % (0.01 * i)) for i in range(1, (100 + 1))]
    color = []

    color.append(0.0)
    color.append(random.choice(nums))
    color.append(0.0)

    return tuple(color)

def randblue():
    nums = [float('%.2f' % (0.01 * i)) for i in range(1, (100 + 1))]
    color = []

    color.append(0.0)
    color.append(0.0)
    color.append(random.choice(nums))

    return tuple(color)
