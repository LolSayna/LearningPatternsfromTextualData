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


def replaceAt(pattern, position, element):
    # inserts one element at a specific position, since strings cant be easily changed
    # pattern(string) -> pattern(string)

    return pattern[:position] + element + pattern[position + 1 :]


def metricLongestCommonSubstring(originalPattern, newPattern):

    if originalPattern == newPattern:
        return 1.0

    lcs = ""

    for i in range(len(originalPattern)):

        subString = ""
        for j in range(len(newPattern)):
            if i + j < len(originalPattern) and originalPattern[i + j] == newPattern[j]:
                subString += newPattern[j]
            else:
                if len(subString) > len(lcs):
                    lcs = subString
                subString = ""

    # print("tmp", len(lcs), len(newPattern))
    return len(lcs) / len(newPattern)