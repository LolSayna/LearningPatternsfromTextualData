import random
import string
from learning_Util import *


def generateRegularPattern(length, varCount, alphabet = string.ascii_lowercase):
    # generates a random regular pattern
    # - length: with a length smaller then the maxLength
    # - varCount: number of Variables
    # - alphabet: the list of characters for the terminals, can be a string in alphabet form or a list in integer list form

    if varCount > length:
        print("more variables then symbols")
        return None

    pattern = []

    for _ in range(length):
        if type(alphabet) is str:
            t = (ord(random.choice(alphabet)) - ord("a")) * 2 + 1
        elif type(alphabet) is list:
            t = random.choice(alphabet)
        pattern.append(t)

    varPos = random.sample(range(length), varCount)
    
    for i, varPos in enumerate(sorted(varPos)):
        pattern[varPos] = i * 2

    return pattern

def generateRepeatingPattern(length, varCount, alphabet = string.ascii_lowercase, repetitions = 3):
    # generates a random one repeating pattern, with "0"/"A" being the repeating variable, 
    # the total repetitions of the repeating variable can higher by 1, since "0" is already once in the pattern, but it can be overwriten or not
    # also can the total number of variables be lower then varCount, since random symbols get overwritten by the repeating variable
    # - repetitions: the nubmer of times the repeating variable gets inserted into the pattern

    repeatingVar = 0

    pattern = generateRegularPattern(length, varCount, alphabet)

    varPos = random.sample(range(len(pattern)), repetitions)

    for pos in varPos:
        pattern[pos] = repeatingVar

    return pattern

def generateWordFromPattern(pattern, subLength = [1,3], alphabet = string.ascii_lowercase, repeatingVar = None):
    # generates a random word for a given pattern:
    # - subLength: the minium and the maximum length for the replacement
    # - alphabet: the list of characters that get replaced for the variable, can be string in alphabet form or a list in integer list form
    # - repeatingVar: adds the option to declare on variable as a repeating

    word = []

    # incase theres a repeating variable it gets genereated first
    if repeatingVar is not None:
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


def randomSampleRegular():
    
    # nr of genereted patterns
    patternCount = 50
    # length of the patterns
    length = 20
    # nr of variables in pattern
    varCount = 5
    # alphabet for the pattern
    alphabet = string.ascii_lowercase

    patterns = []
    for _ in range(patternCount):
        patterns.append(generateRegularPattern(length, varCount, alphabet=alphabet))

    #writeToFile("random/regularPatterns", "RegularPatterns, "+ str(patternCount), patterns)
    # possible to end function here and save the patterns


    # next a tupel form a pattern and words from it are generated

    # nr of words per pattern
    wordCount = 100
    # range for replacement length per variable
    subLength = [1,5]
    # replacement alphabet
    repAlphabet = [1,3,5]

    tupels = []
    for p in patterns:
        words = []
        for _ in range(wordCount):
            words.append(generateWordFromPattern(p, subLength=subLength, alphabet=repAlphabet))
        tupels.append((p, words))
    
    #writeToFile("random/regularWithWords", "RegularPatterns with words, "+ str(patternCount), tupels)

    return tupels
    

def randomSampleOneRep():
    
    # nr of genereted patterns
    patternCount = 50
    # length of the patterns
    length = 30
    # nr of variables in pattern
    varCount = 10
    # alphabet for the pattern
    alphabet = string.ascii_lowercase
    # repetions for the repeting var
    repetitions = 5

    patterns = []
    for _ in range(patternCount):
        patterns.append(generateRepeatingPattern(length, varCount, alphabet=alphabet, repetitions=repetitions))

    #writeToFile("random/oneRepPatterns", "OneRep Patterns, "+ str(patternCount), patterns)
    # possible to end function here and save the patterns


    # next a tupel form a pattern and words from it are generated

    # nr of words per pattern
    wordCount = 100
    # range for replacement length per variable
    subLength = [1,5]
    # replacement alphabet
    repAlphabet = [1,3,5]

    tupels = []
    for p in patterns:
        words = []
        for _ in range(wordCount):
            words.append(generateWordFromPattern(p, subLength=subLength, alphabet=repAlphabet, repeatingVar=0))
        tupels.append((p, words))
    
    #writeToFile("random/oneRepWithWords", "OneRepeatedPatterns with words, "+ str(patternCount), tupels)

    return tupels

if __name__ == "__main__":
    # some testcases

    """
    print(generateRegularPattern(50, 10))
    print(generateRegularPattern(20, 10))
    print(generateRegularPattern(20,5, alphabet="aaaab"))
    print(generateRegularPattern(20,5, alphabet=[5,7,91]))
    """
    """
    print(generateRepeatingPattern(20,5))
    print(generateRepeatingPattern(20,5, repetitions=5))
    print(generateRepeatingPattern(50,5, repetitions=10))
    """
    """
    print(generateWordFromPattern([1, 3, 5, 6]))
    print(generateWordFromPattern([0, 5, 2, 5, 4, 5, 6], alphabet="abbbbbb"))
    print(generateWordFromPattern([0, 51, 51, 51, 6], alphabet=[5,7,91]))
    print(generateWordFromPattern([50, 33, 0, 3, 47, 2, 11, 4, 47, 37, 25, 8, 33, 37, 9, 11, 46, 3, 25, 43, 50, 49],repeatingVar=50))
    """
    randomSampleRegular()
    randomSampleOneRep()

