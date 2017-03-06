""" hash-table.py | Mon, Mar 06, 2017 | Roman S. Collins

    Hash table function written in Python.

"""
import os, time

rows, columns = os.popen('stty size', 'r').read().split()
rows, columns = int(rows), int(columns)

class Hashie:
    def __init__(self, items=[None]):
        self.items = items
        self.table = []

        if len(self.items) > 0: # Account for up to three collisions
            for x in range(len(self.items)):
                for n in range(3):
                    self.table.append(None)

            for x in self.items: # Populate the table
                self.table[(x % len(self.table))] = x

    def ret_table(self):
        return self.table

    def get_item(self, item):
        return self.table[(item % len(self.table))]

    def check_table(self, x): # Check if all x in table
        iterator = 0

        for i in x:
            if i in self.table:
                iterator += 1

        return (iterator == len(x))

def main():
    """ Presumably case 2 takes longest because it is the very
        first collision.

        But I'm not sure...
    """
    testcases = [(54, 26, 93, 17, 77, 31, 44), # No collision
                 (54, 26, 93, 17, 77, 31, 44, 44), # No collision
                 (54, 26, 93, 17, 77, 31, 44, 44, 77)] # Collision

    for x in testcases:
        hash_table = Hashie(x)

        print("{}\033[1;32mCASE: \033[1;m{}{}".format((' ' * ((columns // 2) - (len('CASE: ') + len(x)))), x, (' ' * (columns // 2))))
        print("{}".format(('_' * columns)))

        print("\033[1;32mTABLE: \033[1;m{}\n".format(hash_table.ret_table()))

        starttime = time.time()
        print("\033[1;32mRETURN 93: \033[1;m{}\n".format(hash_table.get_item(x[2])))
        endtime = time.time()

        print("\033[1;32mALL IN TABLE: \033[1;m{}\n".format(hash_table.check_table(x)))

        print("{}{}{}".format((0), (endtime - starttime), (0)))

        print("{}".format(('_' * columns)))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
