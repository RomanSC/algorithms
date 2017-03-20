""" seirpinski.py | Thu, Mar 02, 2017 | Roman S. Collins

    Drawing a Seirpinski triangle using Zelle Graphics
    and recursion.

"""
from graphics import *

class SeirpinskiTriangle():
    def __init__(self):
        self.window = GraphWin('Seirpinski', 800, 600)

    def triangle(self, x0, y0, x1, y1, x2, y2, color='green'):
        # Draw triangle using polygon
        point1 = Point(x0, y0)
        point2 = Point(x1, y1)
        point3 = Point(x2, y2)

        # Polygon
        poly = Polygon(point1, point2, point3)
        poly.setFill(color)
        poly.draw(self.window)

    def seirpinski(self, x0, y0, x1, y1, x2, y2, depth):
        if depth <= 0:
            return

        depth -= 1

        xc = [((x0 + x1) / 2), ((x1 + x2) / 2), ((x2 + x0) / 2)]
        yc = [((y0 + y1) / 2), ((y1 + y2) / 2), ((y2 + y0) / 2)]

        self.triangle(xc[0], yc[0], xc[1], yc[1], xc[2], yc[2], 'white')

        self.seirpinski(x0, y0, xc[0], yc[0], xc[2], yc[2], depth)
        self.seirpinski(x1, y1, xc[0], yc[0], xc[1], yc[1], depth)
        self.seirpinski(x2, y2, xc[1], yc[1], xc[2], yc[2], depth)


def main():
    # Init
    tri = SeirpinskiTriangle()

    # X and Y coords
    xs = [600, 450, 300]
    ys = [450, 300, 450]

    # Draw first triangle
    tri.triangle(xs[0], ys[0], xs[1],ys[1], xs[2],ys[2], 'red')

    # Seirpinski using recursion
    tri.seirpinski(xs[0], ys[0], xs[1],ys[1], xs[2],ys[2],  10)

    # Don't close until enter is pressed.
    wait = input('Done! Type Enter to close: ')

if __name__ == '__main__':
    main()
