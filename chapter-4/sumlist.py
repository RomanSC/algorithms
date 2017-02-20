""" sumlist.py | Sun, Feb 19, 2017 | Roman S. Collins

    From Problem Solving with Algorithms and Data Structures.

    How recursion is used to sum a list of numbers.

    In Python by default as sum()

"""

def one_sumit(unsumlist):
    cur_sum = 0
    for n in unsumlist:
        cur_sum += n

    return cur_sum

def two_sumit(unsumlist):
    if len(unsumlist) == 1:
        return unsumlist[0]
    else:
        # From the book doesn't really work.
        #return unsumlist[0] + unsumlist[1:]

        # So I wrote this monstrousity
        cur_num = unsumlist[0]
        gonext = 0
        total = 0

        while not cur_num == unsumlist[:]:
            if gonext >= len(unsumlist):
                return total

            cur_num = unsumlist[gonext]
            total += cur_num
            gonext += 1

def three_sumit(unsumlist):
    # Have an idea...
    if len(unsumlist) == 1:
        return unsumlist[0]
    else:
        # Nope that's a generator, oh well
        total = ((unsumlist[0] + i) for i in unsumlist[1:])

        return total


def main():
    nums = [1, 4, 54, 62, 108, 2, 1, 3, 40, 55, 300]
    print(one_sumit(nums))

    print(two_sumit(nums))

    print(three_sumit(nums))

if __name__ == '__main__':
    main()


