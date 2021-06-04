import string

"""
The basic definitions, and simple operations on single patterns

"""

# Definitons
# single terminal word -> string
w1 = "abbaabaa"
w2 = "baabbabaabba"
w3 = "abaaaba"
w4 = "abcdefghijklmnopqrstuvwxyz"

# pattern -> string, where capital letters are variables, lower case are terminal symbols
alpha = "aAbaBa"
gamma = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# set of variable assignments -> list of strings for each variabel, the first one fills the first variabel and so on
var = ["lol", "abc", "edf"]


# Integer Array system
# to have more then 26 different variables or terminal symbols, integers are used instead of characters
# all even numbers are variables, starting with 0
# all uneven nubmers are terminals, starting with 1

# all characters can be translated into numbers, except Z and z: A->0, a->1, B->2, b->3,..., Y->48, y->49
# the numbers continue afterwards, and could be translated back into a Z and its int number behind it: 50-> Z50, 51->z51
delta = [0,1,2,3,4,5,6]
epsi = [46,47,48,49,50,51,52,53,1000,99999]

def isVariable(i):
    # as defined in the Int Array, an even number is a variable
    return i % 2 == 0

def convertToAlphabet(pattern):
    # converts a pattern from the int array form, into the alphabet form
    pat = ""
    for c in pattern:
        # since Z is excluded, there are 25 lowercase and 25 uppercase characters
        if c < 50:
            if isVariable(c):
                pat += string.ascii_uppercase[int(c/2)]
            else:
                pat += string.ascii_lowercase[int(c/2)]
        else:
            if isVariable(c):
                pat += "Z" + str(c)
            else:
                pat += "z" + str(c)

    return pat
#print(convertToAlphabet(delta))
#print(convertToAlphabet(epsi))

def convertToIntarray(pattern):
    # converts a pattern form the alphabet form, into the int array system
    pat = []
    for i, c in enumerate(pattern):

        # an uppercase character means a variable
        if ord("A") <= ord(c) <= ord("Y"):
            # since all variables are even, the integer gets multiplied by 2
            pat.append((ord(c) - ord("A")) * 2)

        # a lowercase character means a terminal
        elif ord("a") <= ord(c) <= ord("y"):
            pat.append((ord(c) - ord("a")) * 2 + 1)
        
        # a Z/z is usually followed by its number behind it, so it can easily added into the array
        # if theres no number behind it converts Z-> Z50, z->z51
        elif c == "Z" or c == "z":

            #find how long the number is
            j = 1
            while(i+j < len(pattern) and pattern[i+j].isdigit()):
                j += 1
                
            # check if a number was behind the z
            if j > 1:
                pat.append(int(pattern[i+1:i+j]))
            else:
                if c == "Z":
                    pat.append((ord(c) - ord("A")) * 2)
                else:
                    pat.append((ord(c) - ord("a")) * 2 + 1)

    return pat
#print(convertToIntarray(gamma))
#print(delta)
#print(convertToAlphabet(delta))
#print(convertToIntarray(convertToAlphabet(delta)))
#print(epsi)
#print(convertToAlphabet(epsi))
#print(convertToIntarray(convertToAlphabet(epsi)))



# Operations on one single pattern
def removeVariablesInRow(pattern):
    # trims the pattern when variables are directly after each other, aka aABCb -> aAb
    i = 0
    while i < len(pattern) - 1:
        if isVariable(pattern[i]) and isVariable(pattern[i + 1]):
            pattern.remove(pattern[i + 1])
        else:
            i += 1
    return pattern
#print(removeVariablesInRow([0,2,3,4,6,7,9]))

def canonicalForm(pattern):
    # transforms a pattern into its canonical form
    # this is done by renaming each variable, depending on their occurence

    conversion = {}
    varCounter = 0

    # a dictionary is created, so each time a variable occures it can be checked if it occured before
    for i, c in enumerate(pattern):
        if isVariable(c):

            # if its in the dict a new variable name is already assigned
            try:
                pattern[i] = conversion[c]
            
            # otherwise create one and raise the counter by 2, so the next even number can be used as variable
            except KeyError:
                pattern[i] = conversion[c] = varCounter
                varCounter += 2

    return pattern
#print(canonicalForm([2,2,2,2,2,22,44,44,22,2,2,1,0,0,2,2,22]))

def isRegularPatternClass(pattern):
    # checks if a pattern belongs to the regular pattern class
    # aka no variable occures more then once

    marked = []
    for c in pattern:
        if isVariable(c):
            if c in marked:
                return False
            else:
                marked.append(c)

    return True
#print(isRegularPatternClass([0,2222,2,6,7,7,9,444]))
#print(isRegularPatternClass([0,2222,2,444,6,7,9,444]))

def findAllNonVariables(pattern):
    # aka the maximal terminal factors
    # finds all the parts of the pattern that are not variables, including the suffix and prefix seperated
    # pattern -> list of words(string)

    words = []
    prefix = []
    suffix = []
    w = []

    i = 0
    while i < len(pattern) and not isVariable(pattern[i]):
        prefix.append(pattern[i])
        i += 1

    for c in pattern[len(prefix) :]:
        if isVariable(c):
            if w:
                words.append(w)
                w = []
        else:
            w.append(c)

    suffix = w

    return words, prefix, suffix
#print(findAllNonVariables([0]))
#print(findAllNonVariables([0,7,7,2,3,3,2]))
#print(findAllNonVariables([1,1,0,7,7,2,3,3,2]))
#print(findAllNonVariables([0,7,7,2,3,3,2,5,5]))
#print(findAllNonVariables([1,1,0,7,7,2,3,3,2,5,5]))

# something with oneRep patterns, not IntArray compartible
def findMaximalTerminalFactors(pattern):
    words, prefix, suffix = findAllNonVariables(pattern)

    factors = []
    if prefix:
        factors.append(prefix)

    for fact in words:
        factors.append(fact)

    if suffix:
        factors.append(suffix)

    return factors

"""
not needed in intArray

def replaceAt(pattern, position, element):
    # inserts one element at a specific position, since strings cant be easily changed
    # pattern(string) -> pattern(string)

    return pattern[:position] + element + pattern[position + 1 :]
"""