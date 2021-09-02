import timeit
from learning_randomdata import *
#from learning_biodata import *
from learning_Patterns import *
import matplotlib.pyplot as plt

# the metrics are used to evaluate the generated pattern, is it close to the unknown orgiginal pattern or is it not precise

def metricVarCount(pattern):
    count = 0
    for c in pattern:
        if isVariable(c):
            count += 1
    
    return count

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


def metricByWordMatching(originalPattern, newPattern, testCount, replaceMin, replaceMax):
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


def randomTest(sameplSize=20):

    # vars for the pattern:
    patLength, varCount = 10, 3
    # vars for the sample
    sameplSize, replaceMin, replaceMax = 50, 3, 5
    # vars for testing
    testCount = 1000

    pattern = generateRegularPattern(patLength, varCount)
    sample = generateWordsFromPattern(pattern, sameplSize, replaceMin, replaceMax)
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

# outdated version, look at learn and check test
def graphOne():
    # change to sample size to test whether the descPattern "finds" the pattern the sample is based on
    # x-axis is the sample size
    # y-axis is the lcs percantage

    data = []
    sampleValues = range(1, 100, 1)
    for sampleSize in sampleValues:

        subset = 0.0
        for _ in range(50):

            pattern = generateRegularPattern(10, 3)
            sample = generateWordsFromPattern(pattern, sampleSize, 3, 5)
            newPattern = descPat(sample)
            print(sampleSize, sample)
            print(pattern, newPattern)
            subset += metricLongestCommonSubstring(pattern, newPattern)
            # print(metricLongestCommonSubstring(pattern, newPattern))
        print(subset / 100)
        data.append(subset / 100)

    print(data)

    plt.plot(sampleValues, data)
    plt.xlabel("total sampleSize")
    plt.ylabel("Percentage")
    plt.title("Influenze of sampleSize")
    plt.show()


#graphOne()

#---------------------------------------Tests------------------------------------------#

def viabilityTest():
    
    length = 50
    varCount = 10
    lengthRange = [50,100]
    #alphabet = string.ascii_lowercase
    alphabet = "abcd"

    wordcount = 100
    repetitions = 100

    #only for one repeated:
    repeatingVarTime = 5
    repeatingVar = 0    # since random patterns always have the repeating var 0

    randomWordTimeTotaltime, matchingWordTimeTotaltime = 0, 0

    for _ in range(repetitions):
        #pattern = generateRegularPattern(length, varCount,alphabet=alphabet)
        pattern = generateRepeatingPattern(length, varCount,alphabet=alphabet, repetitions=repeatingVarTime)
        words = []
        for _ in range(wordcount):
            words.append(generateRandomWord(lengthRange,alphabet=alphabet))
        
        start_time = timeit.default_timer()
        for w in words:
            #matchingRegular(pattern, w)
            matchingOneRep(pattern,w)

        randomWordTime = timeit.default_timer() - start_time

        words = []
        for _ in range(wordcount):
            words.append(generateWordFromPattern(pattern,alphabet=alphabet))
        
        start_time = timeit.default_timer()
        for w in words:
            #matchingRegular(pattern, w)
            matchingOneRep(pattern,w)

        matchingWordTime = timeit.default_timer() - start_time

        randomWordTimeTotaltime += randomWordTime
        matchingWordTimeTotaltime += matchingWordTime
        
    print(format(randomWordTimeTotaltime/repetitions, ".5f"), format(matchingWordTimeTotaltime/repetitions, ".5f"))

#viabilityTest()

def varCountTest():

    tupels = randomSampleRegular()
    #tupels = randomSampleOneRep()
    totalVarCount = 0
    for t in tupels:
        (pattern, words) = t
        sample = words

        newpat = descPat(sample)
        #newpat = descPat(sample, matchingFunction=matchingOneRep, classMembershipFunction=isOneRepPatternClass)

        totalVarCount += metricVarCount(newpat)
        print(pattern, newpat)
        print(metricVarCount(pattern), metricVarCount(newpat))
    
    print(f"{totalVarCount/ len(tupels) = }")

#varCountTest()

def learnAndCheck(learnSample, testSample, matchingFunction=matchingRegular, classMembershipFunction=isRegularPatternClass):
    # lerns a descriptive pattern from the sample and returns how many of the words from the testSample were matched
  
    #learnedPattern = descPat(learnSample)
    learnedPattern = descPat(learnSample, matchingFunction, classMembershipFunction)

    count = 0
    for w in testSample:
        if matchingFunction(learnedPattern, w):
            count += 1

    return learnedPattern, count

def learnAndCheckTest():
    testSampleSize = 50

    testSampleSizeRange = range(2, 60)

    dataPoints = []
    for sampleSize in testSampleSizeRange:
        
        matches = 0

        # runs are used to minimize extreme random cases
        runs = 10
        for _ in range(runs):
            tupels = randomSampleRegular(sampleSize + testSampleSize)
            #print(tupels)
            #tripels = []
            for t in tupels:
                (pattern, words) = t
                learnSample = words[:sampleSize]
                testSample = words[sampleSize+testSampleSize:]
                learnedPattern, count = learnAndCheck(learnSample, testSample)

                #print(pattern)
                #print(learnedPattern)
                #print(count)
                matches += count
                #tripels.append((pattern, learnedPattern,count))
        dataPoints.append((matches/runs)/testSampleSize)
        print((matches/runs)/testSampleSize)
        #writeToFile("results/regularLearnAnchCheck", "learnAndCheck: one pattern, a learned from it, the number ob matches words form the sample of size: "+ str(testSampleSize), tripels)
        
        
    print(dataPoints)
    plt.plot(testSampleSizeRange, dataPoints)
    plt.xlabel("Number of words used to learn the pattern")
    plt.ylabel("Number of words matched from 100 possible words")
    #plt.title("Matching words from the original pattern by learned pattern")
    plt.savefig("learnAndCheckTest.png")
    plt.show()

#learnAndCheckTest()

if __name__ == "__main__":

    # print(metricLongestCommonSubstring("aaaaaaaaaabc", "aaaaaaaaaaaabc"))
    # print(metricByWordMatching("aaXbbbbYcac", "aXbYc", 100, 1, 3))

    """
    orgPattern = "aAc"
    sample = ["abc", "abbc", "abbbc"]
    newPattern = descPat(sample)
    print(orgPattern, newPattern)
    """
    # randomTest()
