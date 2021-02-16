from patternUtil import *


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


# print(metricLongestCommonSubstring("vjAjciihCayDktEynlz", "vjAnBlCz"))


def metricByWordMatching(
    originalPattern, newPattern, testCount, replaceMin, replaceMax
):

    sample = generateWordsFromPattern(
        originalPattern, testCount, replaceMin, replaceMax
    )

    found = 0
    for word in sample:
        # print(word)
        if matchingRegular(newPattern, word):
            found += 1

    return float(found) / testCount


# print(metricByWordMatching("vjAjciihCayDktEynlz", "vjAnBlCz", 100, 1,3))
