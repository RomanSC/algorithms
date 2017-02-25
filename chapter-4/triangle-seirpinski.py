from turtle import *

class Triangle:
    def __init__(self, size=400):
        color('#8EFF34', 'black')
        bgcolor('#323C46')

        penup()
        left(90)
        forward(400)
        right(90)
        pendown()
        right(120)

        #speed('slowest')
        speed('fastest')

        self.size = size

        self.points = []

        # For self.col()
        self.n_color = 0
        self.color = ('red', 'blue', 'yellow')

    def draw_triangle(self):
        for i in range(3):
            forward(self.size)
            left(120)
            write(position())
            self.points.append(position())

    def draw_seirpinski(self):
        self.draw_triangle()

        #right(180)

        self.size /= 2

        print(self.col)

        #self.draw_seirpinski()

    def col(self):
        n_color += 1

        return self.color[n_color]

def main():
    tri = Triangle()

    tri.draw_seirpinski()

    wait = input('')

if __name__ == '__main__':
    main()
