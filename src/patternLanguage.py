from knuth_morris_pratt import naive

# single word -> string
w1 = "abbaabaa"
w2 = "baabbabaabba"
w3 = "abaaaba"


# pattern -> string, wo großbuchstaben variablen sind
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

    print(word)
    return word


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


# matching problem for regular pattern, m is number of variables


def matchingRegular(pattern, word):
    """
    # prefix check
    count = 0
    c = pattern[count]
    while c.islower():
        count += 1
        c = pattern[count]
    if pattern[:count] != word[:count]:
        return False
    """

    # main check
    w_i = findAllNonVariables(pattern)

    print(w_i)

    j = 0

    for s in w_i:
        print(j, word[j:], s)
        find = naive(word[j:], s)
        if find == []:
            return False
        else:
            j += find[0] + len(s)

    return True


beta = "aAbaBc"
wort = "abbaabaac"
print(matchingRegular(beta, wort))
