import random
import string
from patternUtil import *


def generateRegularPattern(maxLength, maxVarCount, alphabet = string.ascii_lowercase):
    # generates a random regular pattern, since variables in a row get removed the length might be lower, same for maxVarCount
    # - maxLength: with a length smaller then the maxLength
    # - varCount: number of Variables before variables in a row get trimmed
    # - alphabet: the list of characters for the terminals, can be a string or a list

    if maxVarCount > maxLength:
        print("to many vars")
        return None

    pattern = []

    for _ in range(maxLength):
        if type(alphabet) is str:
            t = (ord(random.choice(alphabet)) - ord("a")) * 2 + 1
        elif type(alphabet) is list:
            t = random.choice(alphabet)
        pattern.append(t)

    varPos = random.sample(range(maxLength), maxVarCount)
    
    for i, varPos in enumerate(sorted(varPos)):
        pattern[varPos] = i * 2

    return canonicalForm(removeVariablesInRow(pattern))

def generateRepeatingPattern(maxLength, maxVarCount, alphabet = string.ascii_lowercase, minRepetitions = 3):
    # generates a random one repeating pattern, "0"/"A" is the repeating variable, 
    # total number of repetitions can be one higher when the variable is already in the generated regular pattern
    # - repetitionRange: the amout of times the repeating variable gets inserted into the pattern
    pattern = generateRegularPattern(maxLength, maxVarCount, alphabet)

    varPos = random.sample(range(maxLength), minRepetitions)

    for pos in varPos:
        pattern[pos] = 0

    return pattern

def generateWordFromPattern(pattern, subLength = [1,3], alphabet = string.ascii_lowercase, repeatingVar = None):
    # generates a random word for a given pattern:
    # - subLength: the minium and the maximum length for the replacement
    # - alphabet: the list of characters that get replaced for the variable, can be a string or a list
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
    #print(generateRegularPattern(20, 10))
    #print(generateRegularPattern(200, 5))
    #print(generateRegularPattern(20,5, alphabet="abbbbbb"))
    #print(generateRegularPattern(20,5, alphabet=[5,7,91]))
    
    #print(generateRepeatingPattern(20,5))
    #print(generateRepeatingPattern(20,5, minRepetitions=5))
    #print(generateRepeatingPattern(50,5, minRepetitions=10))

    #print(generateWordFromPattern(convertToIntarray("ZqAbxBfCxsmEqsefXbmvZy")))
    #print(generateWordFromPattern(convertToIntarray("abcD")))
    #print(generateWordFromPattern(convertToIntarray("abcDeeeeeeeeeeeeeeeeeeeeeeeeeeeeeA"), subLength=(10,20)))
    #print(generateWordFromPattern(convertToIntarray("AcccD"), alphabet="abbbbbb"))
    #print(generateWordFromPattern(convertToIntarray("AzzzD"), alphabet=[5,7,91]))
    #print(generateWordFromPattern(convertToIntarray("ZqAbxBfCxsmEqsefXbmvZy"),repeatingVar=50))
    #print(generateWordFromPattern(convertToIntarray("ZqAbxBfCxsmEqsefXbmvZy"),repeatingVar=50))

    pass
