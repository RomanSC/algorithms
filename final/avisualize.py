#!/usr/bin/python3
""" avisualize.py | Sun, Apr 23, 2017 | Roman S. Collins
"""
import graphics as gfx
import time, sys

width = 400
height = 400

# the main class
class Visualize():
    def __init__(self, title="A* Algorithm"):
        self.screen = gfx.GraphWin(title, width, height, autoflush=True)
        self.screen.setBackground("black")
        self.visualizing = True

        self.x_button = gfx.Rectangle(gfx.Point(width-20, 0), gfx.Point(width, 20))
        self.x_button.setFill("white")

        self.x, self.y = 0, 0

        self.sq = gfx.Rectangle(gfx.Point(self.x, self.y), gfx.Point(self.x+20, self.y+20))
        self.sq.setFill("red")

        # Important -- always last
        self.play()

    def play(self):
        while self.visualizing:
            self.events()
            self.draw()
            self.update()

    def events(self):
        click = self.screen.checkMouse()
        if click:
            if click.x > width - 20 and click.y < 20:
                self.visualizing = False

    def draw(self):
        try:
            self.x_button.draw(self.screen)
            self.sq.draw(self.screen)
        except gfx.GraphicsError:
            pass

    def update(self):
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
        self.x += 1
        self.y += 1

        self.sq.move(1, 1)

        print(self.sq.p1)

        gfx.update()

def main():
    v = Visualize()
    v.play()

    sys.exit()

if __name__ == "__main__":
    main()
