import logging


def naive(text, pattern):
    # navie implementation in O(n*m)

    n, m = len(text), len(pattern)
    matchList = []

    for i in range(n - m + 1):

        matches = 0
        while matches < m and text[i + matches] == pattern[matches]:
            matches += 1

        if matches == m:
            matchList.append(i)

    return matchList


def naiveMulti(text, keywords):

    n = len(text)

    for pattern in keywords:
        m = len(pattern)
        matchList = []

        for i in range(n - m + 1):

            matches = 0
            while matches < m and text[i + matches] == pattern[matches]:
                matches += 1

            if matches == m:
                matchList.append(i)

        return matchList

    return almatches


def createNextTable(pattern):
    # preprocessing function for kmp-algo in O(m), generates preafix-table

    j, t = 0, -1
    prea = [-1]

    for j in range(len(pattern)):

        while t >= 0 and pattern[j] != pattern[t]:

            t = prea[t]

        t = t + 1

        prea.append(t)

    return prea


def knuthMorrisPratt(text, pattern):
    # algo in O(m+n)

    n, m = len(text), len(pattern)
    matchList = []

    # next table
    prea = createNextTable(pattern)
    logging.debug(f"Prefix table in KMP algo: {prea}")

    patPos = 0
    for textPos in range(n):
        while patPos >= 0 and pattern[patPos] is not text[textPos]:
            patPos = prea[patPos]

        patPos = patPos + 1

        if patPos == m:
            matchList.append(textPos - m + 1)
            patPos = prea[-1]

    return matchList

def firstMatchKMP(text,pattern):
    # algo in O(m+n)

    n, m = len(text), len(pattern)

    # next table
    prea = createNextTable(pattern)
    #logging.debug(f"Prefix table in KMP algo: {prea}")

    patPos = 0
    for textPos in range(n):
        while patPos >= 0 and pattern[patPos] is not text[textPos]:
            patPos = prea[patPos]

        patPos = patPos + 1

        if patPos == m:
            return textPos - m + 1

    return None

if __name__ == "__main__":
    # simple test cases
    logging.basicConfig(level=logging.DEBUG)

    text, pattern = "babcbabcabcaabcabcabcacabc", "abcabcacab"
    # text, pattern = "acacacagtaacacagt", "adbfsbvdsfgagdfg"
    print("Text: ", text)
    print("Pattern: ", pattern)
    print("Naive: ", naive(text, pattern))
    print("KMP: ", knuthMorrisPratt(text, pattern))

    print("Naive: ", naive("aaaaa", "aa"))
