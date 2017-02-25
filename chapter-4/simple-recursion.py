""" simple-recursion.py | Sun, Feb 19, 2017 | Roman S. Collins

    Like recursion but simpler.

"""
import sys
from turtle import *
from time import sleep
from turtlecolors import *

sys.setrecursionlimit(30000)

class FullCircle:
    def __init__(self):
        self.full_circle = 0
        self.circle_size = 30
        self.col = 'blue'
        color('blue')
        bgcolor('black')
        pensize(6)
        speed(9 * 999)
        #hideturtle()

        self.tophalf()


    def tophalf(self):
        self.full_circle -= self.full_circle
        for i in range(63):
            forward(self.circle_size)
            left(self.circle_size)
            self.full_circle += 1
            print(position())
        self.bottomhalf()

    def bottomhalf(self):
        self.change_color()
        color(self.col)
        for i in range(63):
            forward(self.circle_size)
            left(self.circle_size)
            self.full_circle += 1
        setposition(0, 0)
        self.tophalf()

    def change_color(self):
        if self.full_circle > 50:
            if self.col == 'blue':
                self.col = 'red'
            elif self.col == 'red':
                self.col = 'blue'

def main():
    FullCircle()

if __name__ == '__main__':
    main()
