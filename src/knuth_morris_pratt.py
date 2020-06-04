import random
import string
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

    return prea


def knuthMorrisPratt(text, pattern):

    matchList = []

    # set the string to start at 1 not 0
    textLen, patLen = len(text), len(pattern)
    text = " " + text
    pattern = " " + pattern

    # next table
    prea = createNextTable(pattern)
    print(prea)

    patPos = textPos = 1
    while textPos <= textLen:

        while patPos > 0 and text[textPos] != pattern[patPos]:

            patPos = prea[patPos]

        textPos = textPos+1
        patPos = patPos+1

        if patPos > patLen:
            matchList.append(textPos-patLen-1)
            patPos = prea[-1]+1

    return matchList

# generate valid inputs


def generateRandom(chars=["a", "b"], length=1000, patternLengthRange=(5, 10)):

    # string.ascii_uppercase + string.digits
    text = "".join(random.choices(chars, k=length))

    patternLenght = random.randrange(
        patternLengthRange[0], patternLengthRange[1])

    patternPos = random.randrange(length-patternLenght)
    pattern = text[patternPos:patternPos+patternLenght]

    return text, pattern, patternPos


# run both alorithms with detailed output
def testBoth(text, pattern):

    print(f"p:{pattern}\nt:{text}")
    print("\nNaive:")
    start = timer()
    print(naive(text, pattern))
    end = timer()
    print(f"In: {end - start:.5f} s")

    print(f"\nWith KMP:")
    start = timer()
    print(knuthMorrisPratt(text, pattern))
    end = timer()
    print(f"In: {end - start:.5f} s\n\n")


# testing if diffrent algorithms lead to diffrent results
def compareResults(times=100):

    for i in range(times):
        text, pattern, pos = generateRandom(length=1000)
        if naive(text, pattern) != knuthMorrisPratt(text, pattern):
            print(print(f"p:{pattern}\nt:{text}"))
            n = naive(text, pattern)
            print(len(n), n)
            k = knuthMorrisPratt(text, pattern)
            print(len(k), k)


# simple test cases
if __name__ == "__main__":

    # compareResults()

    #text, pattern, pos = generateRandom(length=1000)
    #testBoth(text, pattern)

    #testBoth("This is a example text with two is.", "is")
    testBoth("babcbabcabcaabcabcabcacabc", "abcabcacab")
    #testBoth("aaaaaaaaaaaaaaaaaa", "aaa")
