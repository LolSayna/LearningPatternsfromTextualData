import string
from learning_Util import *

from pm_knuth_morris_pratt import firstMatchKMP, knuthMorrisPratt

def matchingRegular(pattern, word):
    # matching problem for regular pattern
    split = splitPattern(pattern)
    m = len(split)

    j = len(split[0])
    if split[0] != word[:j]:
        return False

    #print(f"{split= }, {m= }, {j= }, {split[1:m-1]= }, {split[m-1]= }")

    for w_i in split[1:m-1]:
        if w_i:

            #print(f"{j= }, {word[j+1:]= }, {w_i= }")

            # firstMatchKMP returns the positions where w_i occurs first, but only in the subpattern thats given to it
            # to find the position in the complete word j + 1 needs to be added later
            find = firstMatchKMP(word[j+1:], w_i)

            if find is None:
                return False
            else:

                j += find + len(w_i) + 1
            #print(f"{find= }, new j= {j}")
        else:
            j += 1
    
    #print(f"{split[m-1]= }, {word[j+1:]= }, {j= }")
    if split[m-1] and split[m-1] != word[-len(split[m-1]) :]:
        return False

    return True

#print(matchingRegular([1,2,3,4],[1,1,3,5,5]))

def preProcess(pattern, word, allBetaJs):
    # algo 2 in one rep pattern

    n = len(word)
    
    # each maxmial terminal factor is only needed once
    maxTermFactors = findMaximalTerminalFactors(pattern)
    uniqueMaxTermFactors = [list(x) for x in set(tuple(x) for x in maxTermFactors)] 

    d = {}
    for u in uniqueMaxTermFactors:

        posiblePositons = knuthMorrisPratt(word, u)
        d_i = []
        for i in range(0, n):

            x = list(filter(lambda x: x >= i, posiblePositons))
            
            if x:
                d_i.append(min(x))
            else:
                d_i.append(-1)

        d[tuple(u)] = d_i

   
    # -1 to make it continues with the rest, where there are m+1 betaJ that exits
    m = len(allBetaJs) - 1
    M = [[-1 for _ in range(m+1)] for _ in range(n)]
    """
    print(f"{maxTermFactors = }")
    print(f"{uniqueMaxTermFactors = }")
    print(f"{d = }\n")
    print(f"{m = }")
    print(f"{allBetaJs = }")
    """
    for i in range(0,n):
        for j in range(0,m+1):

            maxTermFactorsBeta = findMaximalTerminalFactors(allBetaJs[j])
            s = len(maxTermFactorsBeta)

            if s == 0:
                # then the bj is a single variable since there are no 2 var direclty after each other
                g = i - 1
                if g < 0:
                    g = None
            else:
                if d[tuple(maxTermFactorsBeta[0])][i] != - 1:
                    g = d[tuple(maxTermFactorsBeta[0])][i] + len(maxTermFactorsBeta[0])
                else:
                    g = None
                
                for h in range(1,s):
                    if g is not None:
                        if d[tuple(maxTermFactorsBeta[h])][i] != - 1:
                            g = d[tuple(maxTermFactorsBeta[h])][i] + len(maxTermFactorsBeta[h])
                        else:
                            g = None

            M[i][j] = g
    return M


# algo 3 with a fixed v
def matchingOneRep(pattern, word):

    # find the repeatingVar
    repeatingVar = findRepeatedVar(pattern)
    # when there is no repeating var, then the pattern is regular
    if repeatingVar is None:
        return matchingRegular(pattern,word)

    factorization = factorisePattern(pattern, repeatingVar)
    m = len(factorization["betaList"])

    M = preProcess(pattern, word, factorization["betaList"] + [factorization["betam+1"]])
    #print(factorization)
    #print(M)
    #print(f"{factorization= } {M = }")

    posZero = len(factorization["w0"])

    if pattern[:posZero] != word[:posZero]:
        #print(f"wrong prefix")
        return False

    factors = findAllFactors(word)


    for v in factors:
        #print(f"current {v = }")
        pos = posZero
        matched = True

        for i in range(0, m):
            #print(i)
            if pos > len(pattern) or M[pos][i] is None:
                matched = False
                break
            else:
                pos = M[pos][i] + 1
            
            alphaj = factorization["wiList"][i] + fillVarWithWord(factorization["gammaList"][i], v, repeatingVar) + factorization["wiDashList"][i]
            #print(f"{alphaj = } {pos = } {len(alphaj) = } {i = }")

            if factorization["betaList"][i] != []:
                find = knuthMorrisPratt(word[pos:], alphaj)
                #print(f"{find = }, {word = }, {alphaj = }")
                if not find:
                    matched = False
                    break
                else:
                    pos = len(alphaj) + find[0]
            else:
                if word[pos:len(alphaj)] != alphaj:
                    matched = False
                    break
                else:
                    pos += len(alphaj)

        if matched:
            #problem with erasing var and the factor of the full word, even if started at pos 0, len(alphaj) = len(pattern) -> therefore remove to long factors
            # cases after all variables

            #print(pattern[pos:])
            if factorization["betam+1"] != []:
                #print(f"{pos = } {m = }")
                if M[pos][m] is not None:
                    pos = M[pos][m]

            if pattern[pos:] == factorization["wim+1"]:
                #print(f"{v = }")
                return True
    return False

#print(matchingOneRep([1,2,1,2,1],[1,5,1,5,1]))

def matchingOneRepNaive(pattern,word):

    repeatingVar = findRepeatedVar(pattern)
    factors = findAllFactors(word)
    
    for v in factors:
        newPattern = []
        [newPattern.extend(v) if c==repeatingVar else newPattern.append(c) for c in pattern]

        if matchingRegular(newPattern, word) is True:
            return True
    return False



def descPat(sample, matchingFunction=matchingRegular, classMembershipFunction=isRegularPatternClass):
    # creates a descriptive pattern from a sample of words, also automatically finds a shortest word

    word = sorted(sample, key=len)[0]

    m = len(word)
    alpha = []
    for i in range(m):
        alpha.append(i*2)
    #print(alpha)

    for i in range(m):
        #print("Current Alpha: ", alpha)

        q, j = True, 0

        # try replacing one variable with one terminal symbol
        newAlpha = alpha.copy()
        newAlpha[i] = word[i]

        # first test is whether the new pattern is still in its pattern class, actually not needed for regualar pattern
        if classMembershipFunction(canonicalForm(newAlpha)):

            # next test if all words from the sample are still in the pattern language
            inSample = True
            for w in sample:
                # print(w, matchingRegular(newAlpha, w))
                if not matchingFunction(newAlpha, w):
                    inSample = False
                    break

            if inSample:
                alpha = newAlpha
                q = False

        # next try to replace variables with each other
        while q and j < i:
            if isVariable(alpha[j]):

                newAlpha = alpha.copy()
                newAlpha[i] = alpha[j]

                if classMembershipFunction(canonicalForm(newAlpha)):

                    # next test if all words from the sample are still in the pattern language
                    inSample = True
                    for w in sample:
                        # print(w, matchingRegular(newAlpha, w))
                        if not matchingFunction(newAlpha, w):
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

if __name__ == "__main__":

    
    # test membership
    alpha = convertToIntList("aAbaBc")
    word1 = convertToIntList("abcbcbcbac")
    word2 = convertToIntList("aaa")
    word3 = convertToIntList("abbasdc")
    #print(alpha,word1,word2)
    #print(matchingRegular(alpha, word1))
    #print(matchingRegular(alpha, word2))
    #print(matchingRegular(alpha, word3))
    #print(matchingRegular([1,2,5,4,9,9], [1,1,1,3,5,7,9]))

    #print(matchingOneRep(alpha, word1, 46))
    #print(matchingOneRep(alpha, word2, 46))
    
    
    sample = [[1,3,3,5,3,3], [1,7,7,5,5,7,7],[1,9,9,3,5,9,9]]
    sample = [[1,3,5],[1,3,3,5],[1,3,3,3,5]]
    #print(descPat(sample, matchingFunction=matchingRegular, classMembershipFunction=isRegularPatternClass))
    #print(oneRepDescPat(sample))
    