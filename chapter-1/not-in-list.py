""" not-in-list.py | Thu, Jan 19, 2017 | Roman S. Collins

    List comprehension excercise from Problem Solving with Algorithms and Data Structures.

    Create a list without duplicate letters from the list ['cat', 'dog', 'rabbit']...

    How I chose to solve the problem vs. the one in the video.

"""
#--- My solution
wordlist = ['cat','dog','rabbit']
letterlist = []
uniqueletters = []

for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)

for y in letterlist:
    if y not in uniqueletters:
        uniqueletters.append(y)

#print(letterlist)
print('My solution: ')
print(uniqueletters, '\n')
#--- My solution

#--- Their solution
print('Their solution: ')
print(list(set([word[i] for word in ['cat', 'dog', 'rabbit'] for i in range(len(word))])))
#--- Their solution

""" What's interesting is that my solution, creates a list in the same exact
    order each time, while theirs seems to have no particular order...
"""
