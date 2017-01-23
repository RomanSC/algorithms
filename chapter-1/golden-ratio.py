""" golden-ratio.py | Sun, Jan 22, 2017 | Roman S. Collins

    Demonstration of the Fibonacci Golden Ratio in Python using
    grids.

"""
import doctest, termcolor

class Gold:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def grid(self, color, n_grids, y_axis, x_axis):
        colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']

        #x_axis += 1
        #y_axis += 1
        #for i in range(n_grids):

        #if color > 4:
        #    color = 0
        #else:
        #    color += 1

        for y in range(y_axis):
            for x in range(x_axis):
                print(termcolor.colored('·', colors[color]), end=' ')
            print('')

def main():
    #ya = 2
    #xa = 2

    #for n in range(3):
    #    ya *= ya
    #    xa += xa
    #    Gold().grid(0, 6, ya, xa)

    Gold().grid(0, 6, 9, 13)

if __name__ == '__main__':
    doctest.testmod()
    main()
