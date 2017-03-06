""" hashie.py | Sun, Mar 05, 2017 | Roman S. Collins

    Hashing function written in Python.

    A hash function should take an input and output
    a non-random (reproducable), unique string.

    Decoding should be the reverse of the hash function.

"""
import sys, math

def parse_file(filename):
    """ Doctest:
        >>> hashme = parse_file("hashme.txt")
        >>> hash_decode(hash_encode(hashme)) == hashme
        True
    """
    letters = []

    with open(filename) as filename:
        for line in filename:
            for l in line:
                # print(l, end='')
                letters.append(l)

    return ''.join(letters)


def hash_encode(inp):
    """ Doctest:
        >>> hash_encode("Hello world!")
        '0x14400x27d90x2d900x2d900x30210x4000x37510x30210x32c40x2d900x27100x441'
    """
    characters = [] # To hold characters

    for l in inp:
        characters.append(ord(l)) # ASCII representation for each character

    for n in range(len(characters)):
        characters[n] = (characters[n] ** 2) # ASCII code squared

    for n in range(len(characters)):
        characters[n] = hex(characters[n]) # Squared ASCII to hex

    hashi = ''.join(characters) # Join full string

    return hashi


def hash_decode(inp):
    """ Doctest:
        >>> print(hash_decode(hash_encode("Hello world!")))
        Hello world!
    """
    # Line 50-56, separate each character
    # at 0x, while inp.split removes 0x
    # which is why loop at 55 is needed
    data = (inp.split('0x'))
    data.pop(0)

    for x in range(len(data)):
        data[x] = '0x' + data[x] # Add '0x'

    for h in range(len(data)):
        # int(n, 16) outputs n in base 16, if n == 0x1440, output: 5184
        # Square root of 5184 is equal to 72.0, convert that to an int
        #
        # Source: Stack Overflow int(n, 16)
        # https://stackoverflow.com/questions/9641440/convert-from-ascii-string-encoded-in-hex-to-plain-ascii
        data[h] = int(math.sqrt(int(data[h], 16))) # Square root of

    for n in range(len(data)):
        # chr(72) == 'H'
        data[n] = chr(data[n]) # Finally convert all ints to chars

    hash_decode = ''.join(data)

    return hash_decode


def main():
    pass
    # print(hash_encode("Hello world!"))
    # print(hash_decode(hash_encode("Hello world!")))

    # hashme = hash_encode(parse_file("hashme.txt"))

    # print(hash_decode(hashme))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
