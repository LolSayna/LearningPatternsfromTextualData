import logging
import string

# assume all char have an int value of less them 256


def generateBadCharRule(pattern):

    badChar = [-1 for c in range(256)]

    for i, c in enumerate(pattern):
        badChar[(ord(c))] = i

    # debug info
    logging.info("Displaying badChar Table:")
    for i, c in enumerate(badChar):
        if c != -1:
            logging.info(f"{chr(i)} {c}")
    return badChar


def generateGoodCharRule(pattern):

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
    logging.info("Displaying goodChar Table Step 1:")
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
    logging.info("Displaying goodChar Table Step 2:")
    logging.info(f)
    logging.info(s)

    return s

# alphabet = List of possible chars in the text


def boyerMoore(text, pattern):

    badChar = generateBadCharRule(pattern)
    goodChar = generateGoodCharRule(pattern)

    matchlist = []

    i = 0
    while i <= len(text)-len(pattern):
        j = len(pattern)-1

        while j >= 0 and pattern[j] == text[i+j]:
            j -= 1

        if j < 0:
            matchlist.append(i)
            i += goodChar[0]
        else:
            i += max(goodChar[j+1], j-badChar[ord(text[i+j])])

    return matchlist


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    print(boyerMoore("kekkekekbekbekbkekkebkeb", "kek"))

    # generateBadCharRule("asdsakodksaodoasdksakdoasdkasodok")
    # generateGoodCharRule("abbabab")
