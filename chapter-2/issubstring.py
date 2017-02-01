"""
"""
class isSubstring:
    # can find foo in barfoobaz
    # but finds ANPANAN in ANPANMAN
    def is_substring(self, substring, string):
        substring  = list(substring)
        string = list(string)

        #y = 0
        #print(substring, string)
        #for i in range(len(string)):
        #    for x in range(len(substring)):
        #        if substring[x] == string[i]:
        #            y += 1
        #            print(string[i])
        #            if y > (len(substring) - 2):
        #                break

        for i in range(len(string)):
            try:
                if string[i] == substring[i]:
                    print(substring[i])
            except IndexError:
                pass

def main():
    """ Doctest:
    >>> print('Hello world!')
    Hello world!
    """
    iss = isSubstring()

    #iss.is_substring('foo', 'barfoobaz')
    iss.is_substring('PAN', 'NAP')

if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()
