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


def generateWordFromPattern(pattern, subLength = [1,3], alphabet = string.ascii_lowercase, repeatingVar = None):
    # generates a random word for a given pattern with the parameters:
    # - subLength: the minium and the maximum length for the replacement
    # - alphabet: the list of characters that get replaced for the variable
    # - repeatingVar: adds the option to declare on variable as a repeating one

    word = []

    # incase theres a repeating variable it gets genereated first
    if repeatingVar:
        rep = []
        for _ in range(random.randint(subLength[0], subLength[1])):
            if type(alphabet) is str:
                t = (ord(random.choice(alphabet)) - ord("a")) * 2 + 1
            elif type(alphabet) is list:
                t = random.choice(alphabet)
            rep.append(t)
        print(rep)

    for c in pattern:

        if c is repeatingVar:
            word += rep
        elif isVariable(c):

            for _ in range(random.randint(subLength[0], subLength[1])):
                if type(alphabet) is str:
                    t = (ord(random.choice(alphabet)) - ord("a")) * 2 + 1
                elif type(alphabet) is list:
                    t = random.choice(alphabet)
                word.append(t)
        else:
            word.append(c)

    return word


if __name__ == "__main__":
    # testing some cases

    #print(generateRegularPattern(20, 5))
    #print(convertToAlphabet(generateRegularPattern(20, 5)))

    print(string.ascii_lowercase)
    
    print(generateWordFromPattern(convertToIntarray("ZqAbxBfCxsmEqsefXbmvZy"),repeatingVar=50))

    
