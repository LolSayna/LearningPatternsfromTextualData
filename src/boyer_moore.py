import logging
import string

# assume all char have an int value of less them 256


def generateBadCharRuleFlens(pattern):
    # https://www.inf.hs-flensburg.de/lang/algorithmen/pattern/bm.htm
    badChar = [-1 for c in range(256)]

    for i, c in enumerate(pattern):
        badChar[(ord(c))] = i

    # debug info
    logging.info("Flens Version: Displaying badChar Table:")
    for i, c in enumerate(badChar):
        if c != -1:
            logging.info(f"{chr(i)} {c}")
    return badChar


def generateBadCharRuleLecroq(pattern):
    # http://www-igm.univ-mlv.fr/~lecroq/string/node14.html#SECTION00140
    badChar = [len(pattern) for c in range(256)]

    for i in range(len(pattern)-1):
        badChar[ord(pattern[i])] = len(pattern) - i - 1

    # debug info
    logging.info("Lecroq Version: Displaying badChar Table:")
    for i, c in enumerate(badChar):
        if c != len(pattern):
            logging.info(f"{chr(i)} {c}")
    return badChar


def generateGoodCharRuleFlens(pattern):

    m = len(pattern)
    f, s = [0 for _ in range(m+1)], [0 for _ in range(m+1)]
    i, j = m, m+1

    f[i] = j
    while i > 0:
        while j <= m and pattern[i-1] != pattern[j-1]:
            if s[j] == 0:
                s[j] = j-i
            j = f[j]
        i -= 1
        j -= 1
        f[i] = j

    # debug info
    logging.info("Flens Version: Displaying goodChar Table Step 1:")
    logging.info(pattern)
    logging.info(f)
    logging.info(s)

    j = f[0]
    for i in range(m+1):
        if s[i] == 0:
            s[i] = j
        if i == j:
            j = f[j]

    # debug info
    logging.info("Flens Version: Displaying goodChar Table Step 2:")
    logging.info(f)
    logging.info(s)

    return s


def generateGoodCharRuleLecroq(pattern):

    m = len(pattern)

    suff = [-1 for _ in range(m)]
    suff[m-1], g = m, m - 1

    for i in range(m-2, -1, -1):
        if i > g and suff[i+m-1-f] < i - g:
            suff[i] = suff[i+m-1-f]
        else:
            if i < g:
                g = i
            f = i
            while g >= 0 and pattern[g] == pattern[g+m-1-f]:
                g -= 1
            suff[i] = f - g

    logging.info(
        f"Lecroq Version: generatetd SuffixTable for goodChar Table: {suff}")

    goodChar = [m for _ in range(m)]
    j = 0

    for i in range(m-1, -1, -1):
        if suff[i] == i + 1:
            while j < m - 1 - i:
                if goodChar[j] == m:
                    goodChar[j] = m - 1 - i
                j += 1

    for i in range(m-1):
        goodChar[m-1-suff[i]] = m - 1 - i

    logging.info(f"Lecroq Version: generatetd goodChar Table: {goodChar}")

    return goodChar


def boyerMooreFlens(text, pattern):

    n, m = len(text), len(pattern)

    badChar = generateBadCharRuleFlens(pattern)
    goodChar = generateGoodCharRuleFlens(pattern)

    matchlist = []

    i = 0
    while i <= n-len(pattern):
        j = m-1

        while j >= 0 and pattern[j] == text[i+j]:
            j -= 1

        if j < 0:
            matchlist.append(i)
            i += goodChar[0]
        else:
            i += max(goodChar[j+1], j-badChar[ord(text[i+j])])

    return matchlist


def boyerMooreLecroq(text, pattern):

    n, m = len(text), len(pattern)

    badChar = generateBadCharRuleLecroq(pattern)
    goodChar = generateGoodCharRuleLecroq(pattern)

    matchlist = []

    j = 0
    while j <= n - m:
        i = m - 1
        while i >= 0 and pattern[i] == text[i+j]:
            i -= 1
        if i < 0:
            matchlist.append(j)
            j += goodChar[0]
        else:
            j += max(goodChar[i], badChar[ord(text[i+j])]-m+1+i)

    return matchlist


def turboBoyerMooreLecroq(text, pattern):

    n, m = len(text), len(pattern)

    badChar = generateBadCharRuleLecroq(pattern)
    goodChar = generateGoodCharRuleLecroq(pattern)

    matchlist = []

    i = 0
    suf = 0
    shift = m
    while i <= n-m:
        j = m-1

        while j >= 0 and pattern[j] == text[i+j]:
            j -= 1
            if suf != 0 and j == m - 1 - shift:
                j -= u

        if j < 0:
            matchlist.append(i)
            shift = goodChar[0]
            suf = m - shift
        else:
            v = m - 1 - j
            turboShift = suf - v
            badCharShift = badChar[ord(text[i+j])] - m + 1 + j
            shift = max(turboShift, badCharShift, goodChar[j])
            if shift == goodChar[j]:
                u = min(m - shift, v)
            else:
                if turboShift < badCharShift:
                    shift = max(shift, suf + 1)
                u = 0
        i += shift

    return matchlist


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    print(boyerMooreLecroq("kekkekekbekbekbkekkebkeb", "kek"))
    print(boyerMooreFlens("kekkekekbekbekbkekkebkeb", "kek"))
    print(turboBoyerMooreLecroq("kekkekekbekbekbkekkebkeb", "kek"))

    #print(turboBoyerMooreLecroq("GCATCGCAGAGAGTATACAGTACG", "GCAGAGAG"))
    # generateBadCharRule("asdsakodksaodoasdksakdoasdkasodok")
    # generateGoodCharRuleLecroq("GCAGAGAG")
