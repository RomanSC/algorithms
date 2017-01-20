""" shakespeare.py | Thu, Jan 19, 2017 | Roman S. Collins

    From Chapter 1 of Problem Solving with Algorithms and Data Structures.

    "Monkey theorem" states that given enough time a monkey hitting keys on
    a typewriter at random will eventual type the complete works of
    William Shakespeare.

    Instead this program replaces the monkey with Python, and Shakespeare's
    complete works with just "methinks it is like a weasel."

"""
import random, termcolor

def main():
    def generateOne(string_length):
        alphabet = 'abcdefghijklmnopqrstuvwxyz '
        result = ''
        for i in range(string_length):
            result += alphabet[random.randrange(27)]

        return result

#    gend = generateOne(len())
#
#    while True:
#        gend = generateOne(len())
#
#        if gend == match_sentence:
#            print(gend)
#            break

    def keepScore(goal, test_string):
        #goal = match_sentence
        num_same = 0

        for i in range(len(goal)):
            if goal[i] == test_string[i]:
                num_same += 1

        return num_same / len(goal)


    match_sentence = 'methinks it is like a weasel'
    new_string = generateOne(28)
    best_score = 0
    new_score = keepScore(match_sentence, new_string)

    #print('test')

    while new_score < 1:
        if new_score <= 0.33:
            color = 'red'
        elif new_score <= 0.66:
            color = 'yellow'
        else:
            color = 'green'

        new_string = generateOne(28)

        if new_score > best_score:
            print(termcolor.colored('{} {}'.format(str(new_score)[0:5], new_string), color))
            best_score = new_score

        #print(new_string)

        new_score = keepScore(match_sentence, new_string)


if __name__ == '__main__':
    main()

