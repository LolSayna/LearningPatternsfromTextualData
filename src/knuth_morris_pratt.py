

def naive(text, pattern):

    patternLenght = len(pattern)
    matchList = []

    for i in range(len(text)-patternLenght+1):

        matches = 0
        while matches < patternLenght and text[i+matches] == pattern[matches]:
            matches += 1

        if matches == patternLenght:

            matchList.append(i)
            print(" " * (i+1), pattern)

    return matchList


def createNextTable(pattern):

    prea = [0] * len(pattern)
    j, t = 1, 0

    while j < len(pattern)-1:

        while t > 0 and pattern[j] != pattern[t]:

            t = prea[t]

        j = j+1
        t = t + 1
        if pattern[j] == pattern[t]:
            prea[j] = prea[t]
        else:
            prea[j] = t

        #print("j: ", j, prea[j])

    return prea

# only finds first match


def knuthMorrisPratt(text, pattern):

    textLen, patLen = len(text), len(pattern)
    text = " " + text
    pattern = " " + pattern

    # next table
    prea = createNextTable(pattern)
    print(prea)

    patPos = textPos = 1
    while patPos <= patLen and textPos <= textLen:

        while patPos > 0 and text[textPos] != pattern[patPos]:

            patPos = prea[patPos]

        textPos = textPos+1
        patPos = patPos+1

        if patPos > patLen:
            # because of leading " " -1
            print(textPos-patLen-1)


def testBoth(text, pattern):

    print(f"Testing normal text:\np:{pattern}\nt:{text}")
    print(naive(text, pattern))

    print(f"\nWith KMP:")
    knuthMorrisPratt(text, pattern)


# simple test cases
if __name__ == "__main__":

    testBoth("This is a example text with two is.", "is")
    testBoth("babcbabcabcaabcabcabcacabc", "abcabcacab")
