import logging
import math

q = 1234567


def rabinKarp(text, pattern):
    # based not on http://www-igm.univ-mlv.fr/~lecroq/string/node5.html

    matchList = []
    n, m, = len(text), len(pattern)

    # preprocessing
    d = 1
    for _ in range(m-1):
        d = (d << 1) % q

    # calc hash(pattern) and hash(the first m char from the text)
    fx, fy = 0, 0
    for i in range(m):
        fx = ((fx << 1) + ord(text[i])) % q
        fy = ((fy << 1) + ord(pattern[i])) % q

    logging.debug(f"Text Hash: {fx} Pattern Hash: {fy}")

    """
    TODO: cleanup work, choos between longer (and repeting) code or an aditional hash operation 
    """

    for i in range(n-m):
        if fx == fy:
            # optional test to only include real matches and not false positiv matches
            logging.debug(
                f"Potential match starting at {i} with the text: {text[i:i+m]}")
            if pattern == text[i:i+m]:
                matchList.append(i)

        fx = (((fx - (ord(text[i]) * d) % q) << 1) % q + ord(text[i+m])) % q
        # print(fx)
        logging.debug(f"New Hash: {fx}")

    # after the last rehash could be a match
    if fx == fy:
        logging.debug(
            f"Potential match starting at {n-m} with the text: {text[n-m:n]}")
        if pattern == text[n-m:n]:
            matchList.append(n-m)

    return matchList


if __name__ == "__main__":
    # simple test cases
    # logging.basicConfig(level=logging.DEBUG)
    pass
    print(rabinKarp("GCATCGCAGAGAGTATACAGTACG", "GCAGAGAG"))
    #print(rabinKarp("10101010101001111010001010111110000101010101", "10100"))
    #print(rabinKarp("standard Text bli bla ble ad fdsdsdsdsd", "bl"))
