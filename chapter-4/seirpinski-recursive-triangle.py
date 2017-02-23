""" seirpinski-recursive-triangle.py | Thu, Feb 23, 2017 | Roman S. Collins

    Seirpinski triangle drawn using Python Turtle.

    Not my code. Hristo Mitev - Source:
    https://www.youtube.com/watch?v=oXagLBxWL44

"""
import math

from turtle import *

def triangle(edge_len):
    for i in range(3):
        forward(edge_len)
        left(120)

def seirpinski(x, y, edge_len):
    if edge_len <= 1: # So that x and y cannot be negative or < 1
        return        # which would cause triangle() to break?

    up()
    goto(x, y)
    down()
    fillcolor('#1c1c46')
    triangle(edge_len)

    seirpinski(x, y, (edge_len / 2)) # Fill triangle
    seirpinski((x + (edge_len / 2)), y, (edge_len / 2)) # Fill
    seirpinski((x + (edge_len / 4)), (y + ((math.sqrt(3) / 4) * edge_len)), (edge_len / 2)) # Fill

def main():
    speed(1)
    #speed(9e10)
    tracer(30, 0)

    color('red', 'black')
    bgcolor('#1c1c46') # Damn Daniel.

    seirpinski(-440, -440, 300) # Starting resolution and triangle size

    while True:
        pass

if __name__ == '__main__':
    main()
