""" recursion.py | Fri, Feb 17, 2017 | Roman S. Collins

    An example of recursion in Python using the turtle
    library.

"""
import sys
from random import choice
from turtle import *
from turtlecolors import *
from time import sleep

sys.setrecursionlimit(30000)

class Turt:
    def __init__(self):
        bgcolor('black')
        speed(9999999999999999999999999999999999999999999999999999999999999999999999999999999)
        #hideturtle()
        self.n = 1
        setposition(0, 0)
        self.pos = position()
        self.testcolor = [0.1, 0.1, 0.1]

    def leftHalf(self):
        color(randblue(), 'black')
        forward(120)
        self.pos = position()

        self.n += 0.08
        self.rightHalf()

    def rightHalf(self):
        color(randblue())
        setposition(self.pos)
        fillcolor(self.shiftcolor())

        begin_fill()
        right(120)
        self.pos = position()
        forward(30 * self.n)
        #setposition(self.pos)
        right(120)
        left(200)
        forward(-60 * self.n)
        color(randgreen())
        fillcolor(self.shiftcolor())
        left(200)
        forward(-60 * self.n)
        setposition(self.pos)
        self.pos = position()
        color(randcolor())
        fillcolor(self.shiftcolor())
        right(400)
        setposition(self.pos)
        forward(70 * self.n)
        left(2)
        self.pos = position()

        self.n += 0.08
        end_fill()
        self.leftHalf()

    def shiftcolor(self):
        ix = -1
        for x in self.testcolor:
            ix += 1
            x += x
            if x > 1.0:
                x = 0.01
            self.testcolor[ix] = x

        return self.testcolor

def main():
    tu = Turt()
    tu.leftHalf()

    while True:
        pass

if __name__ == '__main__':
    main()
