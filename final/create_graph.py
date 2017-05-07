""" create_graph.py | Sun, May 07, 2017 | Roman S. Collins

    A better graph creation function. A link to
    the old crappiness:
    https://pastebin.com/CEM82Pst

    This is better than last because now I can make
    any coordinate a list containing f_scores, g_scores,
    etc.. Also probably more convenient than setting
    up a graph using nodes/vertices represented by a
    class. (Maybe)

"""
from math import inf
from random import choice

# TODO:
# - Obstacles from list
# - Random obstacles
class Create:
    def __init__(self, start, goal, width=5,
                 height=5, start_sym="@", goal_sym="*",
                 rand_obst=False, obst_sym=chr(0x2588),
                 specified=False):
        # start_sym=" @ ", goal_sym=" * ", rand_obst=False, \
        # obst_sym=chr(0x2588), specified=False):

        self.width = width
        self.height = height
        self.tot_obst = 0
        self.obst_num = 0

        self.graph = {}

        for x in range(width):
            # self.graph[x] = x
            tempd = {}
            for y in range(height):
                tempd[y] = inf
                self.graph[x] = tempd

        if specified:
            for i in range(len(specified)):
                # print(self.obst_num)
                # self.graph[specified[i][0]][specified[i][1]] = \
                # str(obst_sym) * self.zero_div(3, self.obst_num)
                # self.obst_num += 1
                # print(self.graph[specified[i][0]][specified[i][1]])
                if specified[i] != start and specified[i] != goal:
                    self.graph[specified[i][0]][specified[i][1]] = \
                    "{}".format(obst_sym * self.obst_str_len(3, self.obst_num))

        """
            Not truely random, I know...

            Because there is a floor to the amount
            of obstacles. But true randomness does
            not exist in CS. So.

        """
        if rand_obst:
            floor = self.width * self.height // 2 # At least 1/2 should be obstacles
            print(floor)
            print(max(self.width, self.height))

            def get_tot(self):
                self.tot_obst = choice([i for i in range(floor,
                                                        max(self.width,
                                                            self.height))])
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

            print(self.tot_obst)
            for x in range(self.tot_obst):
                obst = (choice([i for i in range(0, width)]),
                        choice([i for i in range(0, height)]))
                print(obst)
                self.graph[obst[0]][obst[1]] = \
                "{}".format(obst_sym * self.obst_str_len(3, self.obst_num))

        self.graph[start[0]][start[1]] = \
        "{}".format(start_sym * self.obst_str_len(3, self.obst_num))
        self.graph[goal[0]-1][goal[1]-1] = \
        "{}".format(goal_sym * self.obst_str_len(3, self.obst_num))

    def __str__(self):
        ret_str = ""
        for x in range(self.width):
            ret_str += str(x) + " " + str(self.graph[x]) + "\n"

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
    def __getitem__(self, key):
        return self.graph[key]

    def __setitem__(self, key, val):
        self.graph[key] = val

    """
        For calculating width of obstacles
        more easily (without ZeroDivision
        errors):
    """
    def obst_str_len(self, a, b):
        if a or b == 0:
            return 1
        else:
            return a / b

def main():
    width = 8
    height = 8

    start = (0, 0)
    goal = (8, 8)

    obstacles = [(0, 0), (1, 1), (1, 2), (1, 2),
                 (2, 0), (2, 1), (2, 3), (2, 4)]

    mygraph = Create(start, goal, width, height, rand_obst=True)
    print(mygraph)
    print(mygraph[0][1])

if __name__ == "__main__":
    main()
