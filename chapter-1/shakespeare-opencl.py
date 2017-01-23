""" shakespeare-opencl.py | Thu, Jan 19, 2017 | Roman S. Collins

    From Chapter 1 of Problem Solving with Algorithms and Data Structures.

    "Monkey theorem" states that given enough time a monkey hitting keys on
    a typewriter at random will eventual type the complete works of
    William Shakespeare.

    Instead this program replaces the monkey with Python, and Shakespeare's
    complete works with just "methinks it is like a weasel" or a user
    inputted string.

"""
import random, termcolor, pyopencl, numpy, doctest

#TODO:
# Everything in opencl

class generateString:
    def __init__(self, match_string):
        self.match_string = match_string
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                         'w', 'x', 'y', 'z', ' ']
        self.string_length = len(match_string)

    def __str__(self):
        return self.generate()

    def generate(self):
        gen_string = []

        for i in range(self.string_length):
            gen_string.append(random.choice(self.alphabet))

        gen_string = ''.join(gen_string)

        return gen_string

    def calculate_similarity(self):
        current_string = self.generate()
        similarity = 0

        for i in range(self.string_length):
            if self.match_string[i] == current_string[i]:
                similarity += 1

        similarity = (similarity / self.string_length)

        return similarity, current_string

    def gen_best_match(self):
        similarity, current_string = self.calculate_similarity()
        best = 0
        if similarity > best:
            best = similarity
            return similarity, current_string

def main():
    #print(generateString('weasel'))
    while True:
        #print(str(generateString('weasel').calculate_similarity()))
        #similarity, current_string = generateString('weasel').gen_best_match())
        print(generateString('weasel').gen_best_match())
        #print(simi

if __name__ == '__main__':
    doctest.testmod()
    main()
