""" issubstring.py | Tue, Jan 31, 2017 | Roman S. Collins

    Implementation of Boyer-Moore string search algorithm in Python.

    Source:
    https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm
    https://duckduckgo.com/?q=python+substring+function&t=ffab&ia=q://duckduckgo.com/?q=python+substring+function&t=ffab&ia=qa

"""

class isSubStr:
    string = 'checkoffcheckoofcheckfool'
    substring = 'foo'

    def is_substring(self, substring, string):
        lcolon = 0; rcolon = len(substring); found = False

        for a_iteration in range(len(string) + 1):
            astring = string[lcolon:rcolon]
            lcolon += 1; rcolon += 1; check_char = 0

            for b_iteration in range(len(astring)):
                if astring[b_iteration] == substring[b_iteration]:
                    check_char += 1

                    if check_char == len(substring):
                        found = True

            if found == True:
                return found

            #if astring == substring:
            # Still comparing whole strings
            #    found = True
            #    return found
            #    pass

            if rcolon >= (len(string) + 1):
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

    while isSubStr().is_substring(substring, string):
        break
        print(isSubStr().is_substring(substring, string))

if __name__=='__main__':
    main()
