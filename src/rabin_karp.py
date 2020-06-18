import logging
import math
import random
import sympy
import knuth_morris_pratt


def generateRandomPrime(max):

    p = random.randrange(2, max)
    rerolls = 0

    while not sympy.isprime(p):
        p = random.randrange(2, max)
        rerolls += 1

    logging.info(f"rerolled {rerolls} times, got {p}")

    return p


def convertToBinary(text, pattern):
    binText, binPattern = "", ""
    for c in text:
        binText += f"{ord(c):08b}"

    for c in pattern:
        binPattern += f"{ord(c):08b}"

    return binText, binPattern


def rabinKarp(text, pattern):

    print(text, pattern)
    #text, pattern = convertToBinary(text, pattern)
    print(text, pattern)

    matchList = []

    n, m, = len(text), len(pattern)

    p = generateRandomPrime(int(n*n * m * math.log(n*n * m)))

    fx, fy = int(pattern, base=2) % p, int(text[:m], 2) % p
    print("fy", fx)
    for i in range(n-m):
        if fx == fy:
            matchList.append(i)
        msb = 1 if text[i] == "1" else 0
        nxt = 1 if text[i+m] == "1" else 0

        fx = (2*fx - msb*2 ** m+nxt) % p

    if fx == fy:
        matchList.append(n-m)
        print("lastmatch")

    return matchList


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)

    print(rabinKarp("10101010101001111010001010111110000101010101", "1010"))

    print(rabinKarp("10101010101001111010001010111110000101010101", "10100"))
    #print(rabinKarp("standard Text bli bla ble ad fdsdsdsdsd", "bl"))
