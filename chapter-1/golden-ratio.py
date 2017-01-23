""" golden-ratio.py | Sun, Jan 22, 2017 | Roman S. Collins

    Demonstration of the Fibonacci Golden Ratio in Python using
    grids.

"""
import doctest, termcolor, time
import Fg

class Gold:
    #def __init__(self):
    #    pass
    #
    #def __str__(self):
    #    pass

    def grid(self, n, n_colors, n_list, y_axis, x_axis):
        if n == 6:
            Fg.fg()
            print('')
        else:
            #TODO: Make this work properly
            n_colors = self.n_colors(x_axis)
            for y in range(y_axis):
                for x in range(x_axis):
                    color = n_colors[x]
                    print(termcolor.colored('·', color), end='  ')
                print('')
            print('')

    # Source for fibonnaci:
    # https://www.youtube.com/watch?v=CKPciT2ROL8
    # https://dl.dropboxusercontent.com/u/4904309/fib-spiral.py

    # Over my head:
    # http://sahandsaba.com/five-ways-to-calculate-fibonacci-numbers-with-python-code.html
    def fibby(self, n):
        # let n be number of iterations
        # Gold().fibby(10) returns 55:
        # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
        n_list = []

        n1, n2 = 0, 1
        if (n == 0) or (n == 1):
            return n
        else:
            n_list = [1]
            for iteration in range(n - 1):
                n = n1 + n2
                n1 = n2
                n2 = n
                n_list.append(n)
                """ Breaking it down:
                    Phase 1:
                        n = n1 + n2
                        1
                        n1 = n2
                        1
                        n2 = n
                        1

                    Phase 2:
                        n = n1 + n2
                        2
                        n1 = n2
                        1
                        n2 = n
                        2

                    Phase 3:
                        n = n1 + n2
                        3
                        n1 = n2
                        2
                        n2 = n
                        3
                    Phase 4:
                        n = n1 + n2
                        5
                        n1 = n2
                        3
                        n2 = n
                        5
                    ...
                """
            return n, n_list

    def n_colors(self, n):
        colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']
        n_colors = []

        for i in range(n):
            indx = int(i % len(colors))
            n_colors.append(colors[indx])

        return n_colors

def main():
    # Somethings maths here
    # In 9:13 grid largest
    # Is 8, fibby(6) returns
    # 8
    n = 6

    fn, n_list = Gold().fibby(n)
    n_colors = Gold().n_colors(fn)
    print(fn, n_list, n_colors)
    print('')

    # Stack Overflow - Last item in a list:
    # https://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list-in-python
    # Realized thanks to visual aid that y axis is always
    # the value of last item in the list and x axis always
    # the value of the last item plus the second to last
    ya = int(n_list[-1:][0])
    xa = int(n_list[-2:][0] + n_list[-1:][0])

    Gold().grid(n, n_colors, n_list, ya, xa)

    print('Fibonacci:', len(n_list))
    print('ya =', ya)
    print('xa =', xa)

if __name__ == '__main__':
    doctest.testmod()
    main()
