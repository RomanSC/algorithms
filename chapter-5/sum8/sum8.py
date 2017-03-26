""" sum8.py | Sat, Mar 20, 2017 | Roman S. Collins

    A linear pair search algorithm written in Python

    https://www.youtube.com/watch?v=XKu_SEDAykw&spfreload=10

"""
def haspair(alist, asum):
    stack = []

    for val in alist:
        stack.append(asum - val)
        # print("Stack: ", stack)
        # print("Value: ", val)
        try:
            if stack[-1:][0] + stack[-2:][0] == asum:
                return True
        except:
            pass

    return False

def main():
    mysum = 8
    myvalsa = [1, 2, 3, 9]
    myvalsb = [1, 2, 4, 4]

    result = haspair(myvalsa, mysum)
    print(result)
    result = haspair(myvalsb, mysum)
    print(result)

if __name__ == "__main__":
    main()
