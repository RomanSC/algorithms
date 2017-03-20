from termcolor import *
from turtle import *

class Triangle:
    def __init__(self, size=30):
        color()
        bgcolor()
        speed('slowest')

        self.points = []
        self.mid_points =[]

        self.size = size

    def draw_triangle(self, coord):
        if coord != None:
            penup()
            setposition()
            pendown()

        point = []
        for i in range(3):
            forward(self.size)
            left(120)
            write(i)
            point.append(list(position()))

        self.points.append(point)

        # print(self.points)
        # print('')

    def draw_seirpinski(self):
        coord = None

        self.draw_triangle(coord)

        self.get_midpoints()

    def get_midpoints(self):
        pass
        mid_point = None

        for n in range(len(self.points)):
            print('DEBUG: n = {}'.format(n))
            print('DEBUG: self.points[n] = {}'.format(self.points[n]))
            if n < (len(self.points) - 1):
                #mid_point = None
                mid_point = (self.points[n] + self.points[n + 1] / 2)
                #print(n)
            if mid_point != None:
                self.mid_points.append(mid_point)
        #print(self.points[-1:])

def main():
    tri = Triangle()

    tri.draw_seirpinski()

    wait = input('Done. Press Enter to close: ')

if __name__ == '__main__':
    main()
