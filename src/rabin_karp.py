import logging
import math


def rabinKarp(text, pattern):
    # based not on http://www-igm.univ-mlv.fr/~lecroq/string/node5.html

    matchList = []
    n, m, = len(text), len(pattern)

    # preprocessing
    d = 2**(m-1)

    # calc hash(pattern) and hash(the first m char from the text)
    fx, fy = 0, 0
    for i in range(m):
        fx = 2*fx + ord(text[i])
        fy = 2*fy + ord(pattern[i])

    logging.debug(f"Text Hash: {fx} Pattern Hash: {fy}")

    for i in range(n-m):
        if fx == fy:
            # optional test to only include real matches and not false positiv matches
            logging.debug(
                f"Potential match starting at {i} with the text: {text[i:i+m]}")
            if pattern == text[i:i+m]:
                matchList.append(i)

        fx = ((fx - ord(text[i])*d) * 2) + ord(text[i+m])
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

    print(rabinKarp("estest", "est"))
    print(rabinKarp("GCATCGCAGAGAGTATACAGTACG", "GCAGAGAG"))
    print(rabinKarp("10101010101001111010001010111110000101010101", "10100"))
    print(rabinKarp("standard Text bli bla ble ad fdsdsdsdsd", "bl"))
