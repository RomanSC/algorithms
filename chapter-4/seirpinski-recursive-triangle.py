""" seirpinski-recursive-triangle.py | Thu, Feb 23, 2017 | Roman S. Collins

    Seirpinski triangle drawn using Python Turtle.

    Not my code. Hristo Mitev - Source:
    https://www.youtube.com/watch?v=oXagLBxWL44

"""
import math, sys, time

sys.setrecursionlimit(30000)

from turtle import *

class Seirpinski:
    def __init__(self, x = -475, y = -440, size = (10)):
        pass
        # #speed('slowest')
        # #speed(9e10)
        # speed(3)
        # color('red', 'red')
        # bgcolor('#1c1c46')
        # pensize(2)
        # self.x = x
        # self.y = y
        # self.size = size
        # self.tri_index = 0 # How many triangles have been drawn?

        # self.points = []
        # self.points_swap = []

        color('red', 'red')
        bgcolor('#1c1c46')

        penup()
        left(90)
        forward(445)
        right(90)
        pendown()

        speed('slowest')
        speed('fastest')
        right(120)

        self.x = x
        self.y = y
        self.size = size

        self.points = []

    def draw_triangle(self, itera):
        pass
        # for i in range(3):
        #     forward(size)
        #     left(120)
        #     self.points.append(position())
        #     self.tri_index += 1

        # print(self.points)
        #itera = -1

        # if itera > 0:
        #     if self.points[itera] in self.points:
        #         pass

        for i in range(3):
            forward(self.size)
            left(120)
            #write('{}'.format(itera))
            print('Iteration: {}'.format(itera))

            if (i == 0) or (i == 1):

                # pos = list(position())
                # for z in range(len(pos)):
                #     pos[z] = pos[z] // 1

                if not position() in self.points:
                    self.points.append(list(position()))
                    #print(self.points)
                    #print(len(self.points))

                # self.points.append(position())
                # #print(self.points)
                # print(len(self.points))


        for i in self.points:
            print(i)
        print('\n\n\n')

        itera += 1

        penup()
        setposition(self.points[itera])
        pendown()

        if itera > 300:
            return

        self.draw_triangle(itera)

    def draw_seirpinski(self):
        pass
        # if self.tri_index == 0:
        #     self.draw_triangle(self.x, self.y, self.size) # Outer triangle

        # #self.points = []
        # color('green','green')
        # self.draw_triangle(self.x, self.y, (self.size / 2)) # Triangle 0
        # self.reset_points()

        # color('yellow','yellow')
        # penup()
        # setposition(self.points_swap[2])
        # pendown()
        # self.draw_triangle(self.x, self.y, (self.size / 2)) # Triangle 1
        # self.reset_points()

        # color('purple','purple')
        # penup()
        # setposition(self.points_swap[1])
        # pendown()
        # self.draw_triangle(self.x, self.y, (self.size / 2)) # Triangle 2
        # self.reset_points()

        # color('red','red')

        # #self.size /= 2

        # #sys.exit()

        # self.draw_seirpinski(itera)
        itera = -1

        self.draw_triangle(itera)

        #self.draw_seirpinski()

    def reset_points(self):
        pass
        # self.points_swap = self.points
        # self.points = []

def main():
    pass
    # tri = Seirpinski(x = 0, y = 0, size = 400)
    # #tri = Seirpinski()

    # itera = 0
    # tri.draw_seirpinski(itera) # Starting resolution and triangle size

    # wait = input('Done! Press enter to close: ')
    tri = Seirpinski()


    starttime = time.time()

    tri.draw_seirpinski()

    endtime = time.time()

    print(endtime - starttime)

    wait = input('Done! Press Enter to close: ')

if __name__ == '__main__':
    main()
