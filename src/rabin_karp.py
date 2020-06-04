import logging
import math
import random
import sympy


def generateRandomPrime(max):

    p = random.randrange(2, max)
    rerolls = 0

    while not sympy.isprime(p):
        p = random.randrange(2, max)
        rerolls += 1

    logging.info(f"rerolled {rerolls} times, got {p}")

    return p


def rabinKarp(text, pattern):

    matchList = []

    n, m, = len(text), len(pattern)

    p = generateRandomPrime(int(n*n * m * math.log(n*n * m)))

    fx, fy = int(pattern, base=2) % p, int(text[:m], 2) % p

    for i in range(n-m):
        if fx == fy:
            matchList.append(i)
        msb = 1 if text[i] == "1" else 0
        nxt = 1 if text[i+m] == "1" else 0

        fx = (2*fx - msb*2 ^ m+nxt) % p

    if fx == fy:
        matchList.append(n-m)
        print("lastmatch")

    return matchList


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)

    print(rabinKarp("10101001010111000101100101010", "1010"))
