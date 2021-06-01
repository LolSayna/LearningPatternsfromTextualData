import string

# Definitons
# single terminal word -> string
w1 = "abbaabaa"
w2 = "baabbabaabba"
w3 = "abaaaba"

# pattern -> string, where capital letters are variables, lower case are terminal symbols
alpha = "aAbaBa"

# set of variable assignments -> list of strings for each variabel, the first one fills the first variabel and so on
var = ["lol", "abc", "edf"]


# change to int aray, even numbers are Variables, 0->A, 1->a, 2->B, 3->b,...
w1 = [0,1,2,3,4,5,6,8,0,50,51,52,53,1,1001]

def even(i):
    return i % 2 == 0

def convertString(pattern):
    pat = ""
    for i in pattern:
        if type(i) = int:
            return False
        
    pass

def convertInt(pattern):
    # converts a pattern of variables and terminals from the alphabet form into an int array
    pat = ""
    for i in pattern:
        if i < 52:
            if even(i):
                pat += string.ascii_uppercase[int(i/2)]
            else:
                pat += string.ascii_lowercase[int(i/2)]
        else:
            if even(i):
                pat += " X" + str(int(i/2)) +" "
            else:
                pat += " x" + str(int(i/2)) + " "

    return pat



print("test")
print(convertInt(w1))

# Operations on one single pattern
def removeVariablesInRow(pattern):
    # trims the pattern when variables are directly after each other, aka aABCb -> aAb
    # pattern(string) -> pattern(string)
    i = 0
    while i < len(pattern) - 1:
        if pattern[i].isupper() and pattern[i + 1].isupper():
            pattern = pattern.replace(pattern[i + 1], "")
        else:
            i += 1
    return pattern


def canonicalForm(pattern):
    # transforms a pattern into its canonical form, max number of variables is limited by alphabet size
    # pattern(string) -> pattern(string)

    pattern = list(pattern)

    conversion = {}
    variableName = "A"

    for i, c in enumerate(pattern):
        if c.isupper():
            try:
                pattern[i] = conversion[c]
            except KeyError:
                pattern[i] = conversion[c] = variableName
                variableName = chr(ord(variableName) + 1)

    return "".join(pattern)


def isRegularPatternClass(pattern):
    # checks if a pattern belongs to the regular pattern class
    # pattern(string) -> bool

    for c in string.ascii_uppercase:
        if pattern.count(c) > 1:
            return False

    return True


def findAllNonVariables(pattern):
    # aka the maximal terminal factors
    # finds all the parts of the pattern that are not variables, including the suffix and prefix seperated
    # pattern(string) -> list of words(string)

    words = []
    prefix = suffix = w = ""

    i = 0
    while i < len(pattern) and pattern[i].islower():
        prefix += pattern[i]
        i += 1

    for c in pattern[len(prefix) :]:
        if c.isupper():
            if w != "":
                words.append(w)
                w = ""
        else:
            w += c

    suffix = w

    return words, prefix, suffix


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


def replaceAt(pattern, position, element):
    # inserts one element at a specific position, since strings cant be easily changed
    # pattern(string) -> pattern(string)

    return pattern[:position] + element + pattern[position + 1 :]
