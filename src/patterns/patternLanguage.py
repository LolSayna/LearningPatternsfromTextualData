import sys, os
import pprint

sys.path.append(os.getcwd())

from src.knuth_morris_pratt import naive, knuthMorrisPratt
import string
from patternUtil import *


def preProcess(pattern, word):

    n = len(word)

    maxTermFactors = findMaximalTerminalFactors(pattern)
    d = [[-1 for _ in range(n)] for _ in range(len(maxTermFactors))]

    for dex, u in enumerate(maxTermFactors):
        # print("u: ", u, "ind: ", dex)
        pos = knuthMorrisPratt(word, u)
        # print("pos: ", pos)

        for i in range(0, n):

            x = list(filter(lambda x: x >= i, pos))
            # print("x: ", x)
            if x:

                # print(min(x))
                d[dex][i] = min(x)
    print(d)

    for i in range(0,n):
        # where does m and s come from
        for j in range(0, )


print(preProcess("aaAbbAcc", "aaabbaaccaa"))


def matchingOneRep(pattern, word):
    pass


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

    return canonicalForm(removeVariablesInRow(alpha))


if __name__ == "__main__":

    # test membership
    """
    alpha = "aAbaBc"
    word1 = "abcbcbcbac"
    word2 = "aaa"
    print(matchingRegular(alpha, word1))
    print(matchingRegular(alpha, word2))

    sample = ["abc", "abbc", "abbbc"]
    print(descPat(sample))
    """