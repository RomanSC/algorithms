""" issubstring.py | Tue, Jan 31, 2017 | Roman S. Collins

    Implementation of Boyer-Moore string search algorithm in Python.

    Source:
    https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm
    https://duckduckgo.com/?q=python+substring+function&t=ffab&ia=q://duckduckgo.com/?q=python+substring+function&t=ffab&ia=qa

"""

class isSubStr:
    def is_substring(self, substring, string):
        lcolon = 0
        rcolon = len(substring)

        for iteration in range(len(string)):
            lcolon += 1
            rcolon += 1
            fstring = string[lcolon:rcolon]

            if fstring == substring:
                found = True
                return found

            if rcolon >= len(string):
                found = False
                return found

    def default_is_substring(self, a, b):
        return a in b

def main():
    """ Doctest:
    >>> string = 'ANPANMAN'
    >>> substring = 'PAN'
    >>> print(isSubStr().is_substring(substring, string))
    True
    >>> print(isSubStr().default_is_substring(substring, string))
    True
    """
    string = 'ANPANMAN'
    substring = 'PAN'

    while isSubStr().is_substring(substring, string) == False:
        print('ANPANMAN')

if __name__=='__main__':
    main()
