""" issubstring.py | Tue, Jan 31, 2017 | Roman S. Collins

    Implementation of Boyer-Moore string search algorithm in Python.

    Source:
    https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm
    https://duckduckgo.com/?q=python+substring+function&t=ffab&ia=q://duckduckgo.com/?q=python+substring+function&t=ffab&ia=qa

"""

class isSubStr:
    def is_substring(self, substring, longstring):
        lcolon = 0; rcolon = len(substring); found = False

        for a_iteration in range(len(longstring) + 1):
            astring = longstring[lcolon:rcolon]
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

            if rcolon >= (len(longstring) + 1):
                found = False
                return found

    def default_is_substring(self, a, b):
        return a in b

    # Dylan's substring search algorithm (not my code, please see source):
    # http://pastebin.com/2SB6iAa6
    def dylan_is_substring(self, a, b):
        found = False
        for x in range(len(b)):
            for i in range(len(a)):
                if x + i >= len(b):
                    found = False
                    break
                if a[i] == b[x + i]:
                    found = True
                else:
                    found = False
                    break
            if found:
                break
        return found

    # Jim's substring search algorithm (not my code, please see source):
    # http://cs.marlboro.edu/courses/spring2017/algorithms/code/hw_feb2/substring.py
    def jim_is_substring(self, shortstring, longstring):
        offsets = len(longstring) - len(shortstring) + 1
        if offsets < 1:
            return False
        #else:
        for offset in range(offsets):
            success = True
            for i in range(len(shortstring)):
                if shortstring[i] != longstring[i + offset]:
                    success = False
                    break
            if success:
                return True
        return False

def main():
    """ Doctest:
    >>> string = 'ANPANMAN'
    >>> substring = 'PAN'
    >>> print(isSubStr().is_substring(substring, longstring))
    True
    >>> print(isSubStr().default_is_substring(substring, longstring))
    True
    >>> print(isSubStr().dylan_is_substring(substring, longstring))
    True
    >>> print(isSubStr().jim_is_substring(substring, longstring))
    True
    """
    substring = 'foo'
    fullstring = 'checkoffcheckoofcheckfool'

    #while isSubStr().is_substring(substring, longstring):
    #    break
    print(isSubStr().is_substring(substring, fullstring))
    print(isSubStr().default_is_substring(substring, fullstring))
    print(isSubStr().dylan_is_substring(substring, fullstring))
    print(isSubStr().jim_is_substring(substring, fullstring))

if __name__=='__main__':
    main()
