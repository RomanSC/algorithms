""" raise.py | Thu, Jan 19, 2017 | Roman S. Collins

    Testing raise written about in Problem Solving with Algorithms and Data Structures.

    If a program crashing bug or exception is thrown we can then catch it in Python,
    but we can use raise to change the error message. This is new to me.

    So here's demonstrating raising an exception...

"""
import random

def main():

    boolean = [True, False]

    randbool = random.choice(boolean)

    try:
        import foo
    except:
        pass

    try:
       import bar
    except:
        if randbool == True:
            raise ModuleNotFoundError('An exception was raised. There\'s no such library \"bar\"')
        else:
            print('An exception was not raised. Try running again.')

if __name__ == '__main__':
    main()
