from knuth_morris_pratt import naive, knuthMorrisPratt

# single terminal word -> string
w1 = "abbaabaa"
w2 = "baabbabaabba"
w3 = "abaaaba"


# pattern -> string, where capital letters are variables, lower case are terminal symbols
alpha = "aAbaBa"

# set of variable assignments -> list of strings for each variabel, the first one fills the first variabel and so on
var = ["lol", "abc", "edf"]


def fillPattern(pattern, variables):
    # constructs a single word from a pattern with a given set of variables
    word = ""

    for c in pattern:
        if c.isupper():

            word += variables[ord(c) - ord("A")]
        else:
            word += c

    return word


def canonicalForm(pattern):
    # transforms the pattern into canonical form, for now each variable is unique

    pattern = list(pattern)

    firstVariable = "A"
    for i, c in enumerate(pattern):
        if c.isupper():
            pattern[i] = firstVariable
            firstVariable = chr(ord(firstVariable) + 1)

    return "".join(pattern)


def findAllNonVariables(pattern):
    # finds all the parts of the pattern that are not variables

    words = []

    w = ""
    for c in pattern:
        if c.isupper():
            if w != "":
                words.append(w)
                w = ""
        else:
            w += c

    if w != "":
        words.append(w)

    return words


def matchingRegular(pattern, word):
    # matching problem for regular pattern

    # check prefix
    j = 0
    while pattern[j].islower():
        if pattern[j] != word[j]:
            return False
        j += 1

    # main check
    w_i = findAllNonVariables(pattern)
    suffix = w_i.pop()

    for s in w_i:

        find = knuthMorrisPratt(word[j:], s)
        if find == []:
            return False
        else:
            j += find[0] + len(s)

    # check suffix
    if suffix != word[-len(suffix) :]:
        return False

    return True


def descPat(sample, word):

    m = len(word)

    alpha, var = [], "A"
    for _ in range(m):
        alpha.append(var)
        var = chr(ord(var) + 1)

    for i in range(m):
        q, j = True, 1
        print(alpha)
        # if canonicalForm(fillPattern())

    return alpha


"""
problem: membership problem with variables
fillPattern for single variable
"""

if __name__ == "__main__":

    # test membership
    beta = "aAbaBc"
    word = "abbAabaac"
    # print(matchingRegular(beta, word))

    # print(canonicalForm("AbsdfdsfsdfDefgegegC"))

    sample = ["abc", "abbc", "abbbc"]
    word = "abc"
    print(descPat(sample, word))
