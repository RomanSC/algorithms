""" hash-fun.py | Fri, Mar 20, 2017 | Roman S. Collins

    An example of a simple hash function written in Python.

    A hash function as an "abstract data type" would simply
    take an input and output a unique but not random
    string that would represent the input. The output would
    be reproducible given the same exact input, such as
    a file given as an input.

"""
def hashie(inp):
    split_str = []
    hash_str = 0

    if isinstance(inp, str):
        for letter in inp:
            split_str.append(int(ord(letter)))

        for n in range(len(split_str)):
            split_str[n] = hex(chr(split_str[n]))

        #return split_str

    return hash_str

def main():
    mystring = "Hello world!"

    print(hashie(mystring))

if __name__ == '__main__':
    main()

