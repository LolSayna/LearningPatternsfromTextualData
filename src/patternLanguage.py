from knuth_morris_pratt import naive, knuthMorrisPratt
import string

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

    return pattern[:position] + element + pattern[position + 1 :]


def matchingRegular(pattern, word):
    # matching problem for regular pattern

    w_i, prefix, suffix = findAllNonVariables(pattern)

    # print("Matchint: ", findAllNonVariables(pattern))

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


def findShortestWord(sample):

    return sorted(sample, key=len)[0]


def descPat(sample):

    word = findShortestWord(sample)

    m = len(word)
    alpha = string.ascii_uppercase[:m]

    for i in range(m):
        q, j = True, 0

        # try replacing one variable with one terminal symbol
        newAlpha = replaceAt(alpha, i, word[i])
        print("NEWAPLHA: ", newAlpha)

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

        # next try to improve pattern
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

    return canonicalForm(alpha)


"""
problem: 
cf(αi[xi7→w[i]])∈Π bedeutet test ob pattern noch in pattern classe -> für jede pattern classe eigener test
für regular relativ easy
solved

bis 27.01 regular fertig
dann nächste pattern types
dann real data test

BA struktur:
literatur/erklärungen
implementation beschreiben
test cases
analyse + diagramme

# matching algorithm
# shinohara erklären
# den shinohara algorithmus erklären
# testclassen beschreiben
# über meine implementierung 

"""


if __name__ == "__main__":

    # test membership
    beta = "aAbaBc"
    word = "abbAabaac"
    # print(matchingRegular(beta, word))

    # print(canonicalForm("AbsdfdsfsdfDefgegegC"))

    sample = ["abc", "abbc", "abbbc"]
    print(descPat(sample))

    sample = ["abbaabaa", "baabbabaabba", "abaaaba"]
    word = "abaaaba"
    # print(descPat(sample, word))

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
