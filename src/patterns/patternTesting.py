from patternUtil import *
from patternGenerate import *
from patternLanguage import *

# the metrics are used to evaluate the generated pattern, is it close to the unknown orgiginal pattern or is it not precise


def metricLongestCommonSubstring(originalPattern, newPattern):
    # takes the longestcommonsubstring from poth patterns, ignorig variable or symbol
    # then divides the lcs with the larger length of the patterns
    # -> 1.0 means the strings are equal, 0.5 half of the string is the same

    if originalPattern == newPattern:
        return 1.0

    n, m = len(originalPattern), len(newPattern)
    suff = [[0 for i in range(m + 1)] for j in range(n + 1)]
    res = 0

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                suff[i][j] = 0
            elif originalPattern[i - 1] == newPattern[j - 1]:
                suff[i][j] = suff[i - 1][j - 1] + 1
                res = max(res, suff[i][j])
            else:
                suff[i][j] = 0
    return res / max(n, m)


def metricByWordMatching(
    originalPattern, newPattern, testCount, replaceMin, replaceMax
):
    # generates random words from the originalPattern and tests if the newPattern matches thoose
    # returns the percentage of succsesfull matches

    sample = generateWordsFromPattern(
        originalPattern, testCount, replaceMin, replaceMax
    )

    found = 0
    for word in sample:
        if matchingRegular(newPattern, word):
            found += 1

    return float(found) / testCount


def RandomTest():

    # vars for the pattern:
    patLength, varCount = 10, 3
    # vars for the sample
    wordCount, replaceMin, replaceMax = 50, 3, 5
    # vars for testing
    testCount = 1000

    pattern = generateRegularPattern(patLength, varCount)
    sample = generateWordsFromPattern(pattern, wordCount, replaceMin, replaceMax)
    print("Generated Pattern: ", pattern)
    print("Generated Sample: ", sample)

    newPattern = descPat(sample)
    print("Build Pattern: ", newPattern)

    wordMatching = metricByWordMatching(
        pattern, newPattern, testCount, replaceMin, replaceMax
    )
    lcs = metricLongestCommonSubstring(pattern, newPattern)

    print("LCS: ", lcs)
    print("WordMatching: ", wordMatching)


if __name__ == "__main__":

    # print(metricLongestCommonSubstring("aaaaaaaaaabc", "aaaaaaaaaaaabc"))
    # print(metricByWordMatching("aaXbbbbYcac", "aXbYc", 100, 1, 3))

    """
    orgPattern = "aAc"
    sample = ["abc", "abbc", "abbbc"]
    newPattern = descPat(sample)
    print(orgPattern, newPattern)
    """
    RandomTest()