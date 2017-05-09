#!/usr/bin/python3
""" create_graph.py | Sun, May 07, 2017 | Roman S. Collins

    A better graph creation function. A link to the old crappiness:
    https://pastebin.com/CEM82Pst

    This is better than last because now I can make any coordinate a list
    containing f_scores, g_scores, etc.. Also probably more convenient than
    setting up a graph using nodes/vertices represented by a class. (Maybe)
    And more efficient than using a list of lists.

    Also because, I prefer refering to x and y with:
    graph[x][y]

"""
from math import inf
from random import choice

class GridGraph:
    def __init__(self, start, goal, width=5,
                 height=5, start_sym="@", goal_sym="*",
                 rand_obst=False, obst_sym=str(chr(0x2588)),
                 specified=False):
        # start_sym="@", goal_sym=" * ", rand_obst=False, \
        # obst_sym=chr(0x2588), specified=False):

        self.width = width
        self.height = height
        self.tot_obst = 0
        self.obst_num = 0
        self.start_sym = start_sym
        self.goal_sym = goal_sym
        self.obst_sym = obst_sym

        self.graph = {}

        for x in range(width):
            # self.graph[x] = x
            # tempd = {}
            self.graph[x] = {}
            for y in range(height):
                # tempd[y] = inf
                self.graph[x][y] = inf

        if specified:
            for i in range(len(specified)):
                # print(self.obst_num)
                # self.graph[specified[i][0]][specified[i][1]] = \
                # str(obst_sym) * self.zero_div(3, self.obst_num)
                # self.obst_num += 1
                # print(self.graph[specified[i][0]][specified[i][1]])
                if specified[i] != start and specified[i] != goal \
                and specified[i][1] <= width and specified[i][0] <= height:
                    # self.graph[specified[i][1]][specified[i][0]] = \
                    # "{}".format(obst_sym * self.obst_str_len(3, self.obst_num))
                    self.graph[specified[i][1]][specified[i][0]] = self.obst_sym

        """ Disclaimer:

            Not 'truely random', because there's a floor. Should be close
            enough to test while giving a good amount of obstacles within
            a range. Range could be a range greater than -1 and less than
            graph the boundary.

            Testing astar one might question how efficiently A* finds the
            path for a given percentage of 'randomly' chosen obstacles in a
            set of generated graphs.
        """
        if rand_obst:
            min_obst = self.width * self.height // 3 # At least 1/3 should be obstacles
            max_obst = self.width * self.height - max(self.width, self.height)
            # max_wh = max(self.width, self.height)
            # print(min_obst)
            # print(max_wh)

            def get_tot(self):
                self.tot_obst = choice([i for i in range(min_obst, max_obst)])

            # Probably not most efficient O(n * 1)
            # where n greater than total area of graph
            # If all are greater than O(n ** 2) but...
            # I don't anticipate that I guess.
            """
                There shall never be more obstacles
                than the total area of the graph.

                Source:
                Physics Classroom - Determining the Area on a v-t Graph:
                http://www.physicsclassroom.com/class/1DKin/Lesson-4/Determining-the-Area-on-a-v-t-Graph
            """
            area = self.width * self.height
            get_tot(self)
            if self.tot_obst <= area:
                get_tot(self)

            # print(self.tot_obst)
            for x in range(self.tot_obst):
                obst = (choice([x for x in range(0, width)]),
                        choice([y for y in range(0, height)]))
                # print(obst)
                # self.graph[obst[1]][obst[0]] = \
                # "{}".format(obst_sym * self.obst_str_len(3, self.obst_num))
                self.graph[obst[1]][obst[0]] = self.obst_sym

        # self.graph[start[1]][start[0]] = \
        # "{}".format(start_sym * self.obst_str_len(3, self.obst_num))
        # self.graph[goal[1]-1][goal[0]-1] = \
        # "{}".format(goal_sym * self.obst_str_len(3, self.obst_num))
        self.graph[goal[1]-1][goal[0]-1] = self.goal_sym
        self.graph[start[1]][start[0]] = self.start_sym

    def __str__(self):
        ret_str = ""
        for x in range(self.width):
            ret_str += "X: " + str(self.graph[x]) + " Y: " + str(x) + "\n"

        return ret_str

    """
        Use __getitem__ and __setitem__ methods
        for indexing support and setting info

        Sources:

        - Python Software Foundation, Python Reference.
          #python IRC channel linked me to this after asking,

              "Hey all, is there a way to create a index method
               for a class, I'm getting type error object does
               not support indexing. I am trying to map a graph
               to a dictionary using coords as keys. So when I
               do mygraph[0][1] I want the item, within the
               dictionary containing ys, within the dictionary
               containing xs":

          https://docs.python.org/3/reference/datamodel.html#object.__getitem__
          https://pastebin.com/sc65kegt

    """
    def __getitem__(self, tup):
        if not isinstance(tup, tuple):
            print("Indexing must be done using a tuple for (x, y) coordinates.")
        else:
            return self.graph[tup[1]][tup[0]]

    def __setitem__(self, tup, val):
        self.graph[tup[1]][tup[0]] = val

    """
        For calculating width of obstacles
        more easily (without ZeroDivision
        errors):
    """
    def obst_str_len(self, a, b, f=True):
        # if a or b == 0:
        #     return 1
        # else:
        #     return a / b
        # print(len("\"\""))
        if a == 0:
            return 0
        elif b == 0:
            return a - len("\"\"")
        else:
            if f:
                return a // b - len("\"\"")
            elif not f:
                return a / b - len("\"\"")

def main():
    width = 8
    height = 8

    start = (0, 0)
    goal = (8, 8)

    obstacles = [(0, 3), (1, 3), (2, 3),
                 (3, 3), (4, 3), (5, 3),
                 (6, 3), (7, 3)]

    for o in obstacles:
        print(o, end=" ")

    print("\n")

    # mygraph = GridGraph(start, goal, width, height, rand_obst=True)
    mygraph = GridGraph(start, goal, width, height, specified=obstacles)
    print(mygraph)

    for o in obstacles:
        # print(mygraph[o[0]][o[1]])
        # print(o)
        print(mygraph[(o[0], o[1])], end=" ")

    print("\n")

if __name__ == "__main__":
    main()
