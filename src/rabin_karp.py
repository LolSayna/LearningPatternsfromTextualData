import logging
import math
import random
import sympy
import knuth_morris_pratt


def rabinKarp(text, pattern):

    matchList = []
    n, m, = len(text), len(pattern)

    # preprocessing
    d = 2**(m-1)

    fx, fy = 0, 0
    for i in range(m):
        fx = 2*fx + ord(text[i])
        fy = 2*fy + ord(pattern[i])

    logging.debug(f"Text Hash: {fx} Pattern Hash: {fy}")

    for i in range(n-m):
        if fx == fy:
            # optional test for correction
            logging.debug(
                f"Potential match starting at {i} with the text: text[i:i+m]")
            if pattern == text[i:i+m]:
                matchList.append(i)

        fx = ((fx - ord(text[i])*d) * 2) + ord(text[i+m])
        logging.debug(f"New Hash: {fx}")

    return matchList


if __name__ == "__main__":

    # logging.basicConfig(level=logging.DEBUG)

    print(rabinKarp("GCATCGCAGAGAGTATACAGTACG", "GCAGAGAG"))

    print(rabinKarp("10101010101001111010001010111110000101010101", "10100"))
    print(rabinKarp("standard Text bli bla ble ad fdsdsdsdsd", "bl"))
