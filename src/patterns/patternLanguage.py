import sys, os

sys.path.append(os.getcwd())

from src.knuth_morris_pratt import naive, knuthMorrisPratt
import string
from patternUtil import *
from patternGenerate import *


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


def NewTest():

    for _ in range(10):
        # vars for the pattern:
        patLength, varCount = 25, 3
        # vars for the sample
        wordCount, replaceMin, replaceMax = 2, 1, 3

        # vars for testing
        testCount = 1000

        pattern = generateRegularPattern(patLength, varCount)
        # pattern = "AarfmrBiawpyCrxtte"
        sample = generateWordsFromPattern(pattern, wordCount, replaceMin, replaceMax)

        print(pattern)
        print(sample)

        descPattern = descPat(sample)
        """
        wordMatching = metricByWordMatching(
            pattern, descPattern, testCount, replaceMin, replaceMax
        )
        lcs = metricLongestCommonSubstring(pattern, descPattern)

        print(pattern)
        print(descPattern)
        print(wordMatching)
        print(lcs)
        print("\n")
        """
        # print(sample)


# print(metricByWordMatching("abC", "aBc"))
# print(metricLongestCommonSubstring("abC", "aBc"))
NewTest()


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


"""
tester("aAbcBddeeffChiD", 1, 1000, 4)
tester("aAbcBddeeffChiD", 2, 1000, 4)
tester("aAbcBddeeffChiD", 5, 1000, 4)
tester("aAbcBddeeffChiD", 10, 1000, 4)
tester("aAbcBddeeffChiD", 20, 1000, 4)
tester("aAbcBddeeffChiD", 100, 1000, 4)
tester("aAbcBddeeffChiD", 1000, 1000, 4)
"""

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