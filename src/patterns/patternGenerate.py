import random
import string
from patternUtil import *


def generateRegularPattern(length, varCount):
    # generates a random regular pattern with a length smaller then the length parameter, with varCount number of Variables, returns in string form

    pattern = random.choices(string.ascii_lowercase, k=length)

    varPos = random.sample(range(length), varCount)

    for i, varPos in enumerate(sorted(varPos)):
        pattern[varPos] = chr(ord("A") + i)

    pattern = "".join(pattern)

    pattern = convertToIntarray(pattern)

    return canonicalForm(removeVariablesInRow(pattern))


def generateWordsFromPattern(pattern, wordCount, replaceMin, replaceMax):
    # takes the pattern and generates a word for it, each variable gets replace by a word which length is between replaceMin and replaceMax; generates wordCount words
    # not compatible with new intArray

    words = []
    for _ in range(wordCount):

        word = ""
        for c in pattern:
            if c.isupper():
                for _ in range(random.randint(replaceMin, replaceMax)):
                    word += random.choice(string.ascii_lowercase)
            else:
                word += c
        words.append(word)

    return words


if __name__ == "__main__":
    # testing some cases

    #print(generateRegularPattern(20, 5))
    #print(convertToAlphabet(generateRegularPattern(20, 5)))

    """
    # care with intArray not working
    #print(generateWordsFromPattern("qAbxBfCDxsmEqsefbmvy", 5, 1, 3))

    """
