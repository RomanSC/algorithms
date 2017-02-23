""" not-seirpinski-but-cool.py

    NotSeirpinski's triangle drawn using Python turtle, recursively.

"""
import sys
sys.setrecursionlimit(30000) # How not to write software

from time import sleep # For DEBUG
from turtle import *



class NotSeirpinski:
    def __init__(self, title='NotSeirpinski'): # Use a class to store defaults
        # Triangle
        self.size = 20 # Size of triangle
        self.orig_size = self.size # Track original size
        self.all_points = [] # Positions for each triangle point
        self.n_triangle = 0 # Iterator that counts triangles
        self.switch = 0
        self.start = False

        # Screen resolution
        self.width = (getscreen().window_width() - 12)
        self.height = (getscreen().window_height() - 20)

        self.hw = (self.height // 2)
        self.hh = (self.width // 2)

        # Init
        speed(9e10)
        hideturtle()
        penup() # Center the pen
        setposition(-0, self.hw)
        pendown()
        right(120) # Ready the pen
        color('red', 'black')
        fillcolor('white')
        bgcolor('#1c1c46') # Damn Daniel.

        # Start drawing
        self.draw_full_triangle()


    def draw_triangle(self):
        self.indiv_points = []
        #print(position())

        begin_fill()

        for i in range(3):
            forward(self.size)
            left(120)
            #write(str(i))
            self.indiv_points.append(position())
        end_fill()

        self.n_triangle += 1

        self.all_points.append(self.indiv_points)

    def switch_point(self):
        if self.switch == 1:
            self.switch = 0
        else:
            self.switch = 1

    def draw_full_triangle(self):
        if self.n_triangle == 0:
            self.draw_triangle()
        if self.n_triangle <= 1:
            penup()
            self.draw_triangle()
            setposition(0, 440)
            pendown()
        else:
            self.draw_triangle()

        # if self.n_triangle >= 1:
        #     print('\n{}\n{}'.format(self.all_points, self.n_triangle))
        #     penup()
        #     setposition(self.all_points[(self.n_triangle - 1)][0])
        #     pendown()
        # if self.n_triangle >= 2:
        #     penup()
        #     setposition(self.all_points[(self.n_triangle - 2)][1])
        #     pendown()
        # if self.n_triangle >= 3:
        #     penup()
        #     setposition(self.all_points[(self.n_triangle - 3)][0])
        #     pendown()


        penup()
        setposition(self.all_points[(self.n_triangle // 2)][self.switch])
        self.switch_point()
        pendown()

        # while self.n_triangle < 1:
        #     self.draw_full_triangle()
        # while True:
        #     pass

        self.draw_full_triangle()

class main():
    triangle = NotSeirpinski()

    #triangle.draw_triangle()
    triangle.draw_full_triangle()

    print(getscreen().window_width())
    print(getscreen().window_height())

if __name__ == '__main__':
    main()
