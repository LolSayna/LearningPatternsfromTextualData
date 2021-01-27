from knuth_morris_pratt import naive, knuthMorrisPratt
import string
import random

# single terminal word -> string
w1 = "abbaabaa"
w2 = "baabbabaabba"
w3 = "abaaaba"

# pattern -> string, where capital letters are variables, lower case are terminal symbols
alpha = "aAbaBa"

# set of variable assignments -> list of strings for each variabel, the first one fills the first variabel and so on
var = ["lol", "abc", "edf"]


def fillCompletePattern(pattern, variables):
    # constructs a single word from a pattern with a given set of variables
    word = ""

    for c in pattern:
        if c.isupper():

            word += variables[ord(c) - ord("A")]
        else:
            word += c

    return word


def canonicalForm(pattern):
    # transforms the pattern into canonical form, max number of variables is limited by alphabet

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
    # checks if the pattern belongs to the regular pattern class

    for c in string.ascii_uppercase:
        if pattern.count(c) > 1:
            return False

    return True


def findAllNonVariables(pattern):
    # finds all the parts of the pattern that are not variables

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
    # inserts one element at a specific position

    return pattern[:position] + element + pattern[position + 1 :]


def matchingRegular(pattern, word):
    # matching problem for regular pattern

    w_i, prefix, suffix = findAllNonVariables(pattern)

    j = len(prefix)

    # check prefix
    if prefix != word[:j]:
        return False

    # main check
    for s in w_i:

        find = knuthMorrisPratt(word[j:], s)
        if find == []:
            return False
        else:
            j += find[0] + len(s)

    # check suffix
    # check if the suffix is not empty and only then whether it matches
    if suffix and suffix != word[-len(suffix) :]:
        return False

    return True


def descPat(sample):
    # creates a descriptive pattern from a sample of words, also automatically finds a shortest word

    word = sorted(sample, key=len)[0]

    m = len(word)
    alpha = string.ascii_uppercase[:m]

    for i in range(m):
        # print("Current Alpha: ", alpha)

        q, j = True, 0

        # try replacing one variable with one terminal symbol
        newAlpha = replaceAt(alpha, i, word[i])

        # first test is whether the new pattern is still in its pattern class, actually not needed for regualar pattern
        if isRegularPatternClass(canonicalForm(newAlpha)):

            # next test if all words from the sample are still in the pattern language
            inSample = True
            for w in sample:
                # print(w, matchingRegular(newAlpha, w))
                if not matchingRegular(newAlpha, w):
                    inSample = False
                    break

            if inSample:
                alpha = newAlpha
                q = False

        # next try to replace variables with each other
        while q and j < i:
            if alpha[j].isupper():
                newAlpha = replaceAt(alpha, i, alpha[j])

                if isRegularPatternClass(canonicalForm(newAlpha)):

                    # next test if all words from the sample are still in the pattern language
                    inSample = True
                    for w in sample:
                        # print(w, matchingRegular(newAlpha, w))
                        if not matchingRegular(newAlpha, w):
                            inSample = False
                            break

                    if inSample:
                        alpha = newAlpha
                        q = False
                    else:
                        j += 1
            if q:
                j += 1

    # filter variables in a row
    alpha = canonicalForm(alpha)
    i = 0
    while i < len(alpha) - 1:
        if alpha[i].isupper() and alpha[i + 1].isupper():
            alpha = alpha.replace(alpha[i + 1], "")
        else:
            i += 1

    return canonicalForm(alpha)


def generateWords(numberOfVariables):

    parts = []
    for _ in range(numberOfVariables):
        s = ""
        length = random.randint(3, 5)
        for _ in range(length):
            s += random.choice(string.ascii_lowercase)
        parts.append(s)

    return parts


def tester(pattern, generation, testing, varCount):

    sample = []
    for _ in range(generation):
        sample.append(fillCompletePattern(pattern, generateWords(varCount)))

    descPattern = descPat(sample)

    testPositiv = 0
    for _ in range(testing):
        if matchingRegular(
            descPattern, fillCompletePattern(pattern, generateWords(varCount))
        ):
            testPositiv += 1

    # print(sample)
    print(descPattern)
    print(float(testPositiv) / testing)


tester("aAbcBddeeffChiD", 2, 1000, 4)
tester("aAbcBddeeffChiD", 5, 1000, 4)
tester("aAbcBddeeffChiD", 10, 1000, 4)
tester("aAbcBddeeffChiD", 20, 1000, 4)
tester("aAbcBddeeffChiD", 100, 1000, 4)
tester("aAbcBddeeffChiD", 1000, 1000, 4)


if __name__ == "__main__":
    """
    # test membership
    beta = "aAbaBc"
    word = "abbAabaac"
    print(matchingRegular(beta, word))
    """
    # print(canonicalForm("AbsdfdsfsdfDefgegegC"))

    """
    sample = ["abc", "abbc", "abbbc"]
    print(descPat(sample))
    """

    """
    sample = ["abbaabaa", "baabbabaabba", "abaaaba"]
    print(descPat(sample))
    """
    """
    pattern = "AjisdBijsdCasd"
    sample = [
        fillCompletePattern(pattern, ["sdf", "asfsf", "ogf"]),
        fillCompletePattern(pattern, ["fg", "jgj", "vcbcvb"]),
        fillCompletePattern(pattern, ["werw", "ztz", "ertz"]),
        fillCompletePattern(pattern, ["gfg", "fbd", "drtr"]),
        fillCompletePattern(pattern, ["asd", "zatz", "dfgdfh"]),
        fillCompletePattern(pattern, ["cvs", "zdfertz", "qwewe"]),
        fillCompletePattern(pattern, ["fsd", "gfh", "ere"]),
        fillCompletePattern(pattern, ["werw", "ztz", "yxyx"]),
        fillCompletePattern(pattern, ["asdsd", "fgfd", "asdsf"]),
        fillCompletePattern(pattern, ["uziui", "jijo", "fgjgfj"]),
    ]
    print(sample)
    print(descPat(sample))
    """