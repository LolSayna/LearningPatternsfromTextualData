import random
import string
import logging
from timeit import default_timer as timer


def naive(text, pattern):

    patternLenght = len(pattern)
    matchList = []

    for i in range(len(text)-patternLenght+1):

        matches = 0
        while matches < patternLenght and text[i+matches] == pattern[matches]:
            matches += 1

        if matches == patternLenght:

            matchList.append(i)
            #logging.debug(" " * (i+1), pattern)

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


def knuthMorrisPratt(text, pattern):

    matchList = []

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
            matchList.append(textPos-patLen-1)
            patPos = prea[patPos-1]

    return matchList


def generateRandom(chars=["a", "b"], length=1000):

    #string.ascii_uppercase + string.digits
    text = "".join(random.choices(chars, k=length))

    patternLenght = random.randrange(5, 10)
    patternPos = random.randrange(length-patternLenght)

    pattern = text[patternPos:patternPos+patternLenght]

    return text, pattern, patternPos


def testBoth(text, pattern):

    print(f"p:{pattern}\nt:{text}\nNaive:")
    start = timer()
    print(naive(text, pattern))
    end = timer()
    print(f"In: {end - start} s")

    print(f"\nWith KMP:")
    start = timer()
    print(knuthMorrisPratt(text, pattern))
    end = timer()
    print(f"In: {end - start} s")


# simple test cases
if __name__ == "__main__":

    text, pattern, pos = generateRandom(length=1000)

    testBoth(text, pattern)

    #testBoth("This is a example text with two is.", "is")

    #testBoth("babcbabcabcaabcabcabcacabc", "abcabcacab")
