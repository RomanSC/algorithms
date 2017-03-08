""" seirpinski-triangle.py | Tue, Feb 21, 2017 | Roman S. Collins
"""
from turtle import *

def triangle(n_triangle, size=30):
    points = []
    for i in range(3):
        forward(size)
        left(120)
        points.append(i)

    n_triangle += 1
    tri_points.append(points)

    print(points)

def main():

    tri_points = []
    n_triangle = 0

    for i in range(3):
        triangle(n_triangle)

    wait = input('Done! Press enter to close: ')

if __name__ == '__main__':
    main()
