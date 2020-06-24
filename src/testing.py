import random
from timeit import default_timer as timer
from knuth_morris_pratt import naive
from knuth_morris_pratt import knuthMorrisPratt
from rabin_karp import rabinKarp
from aho_corasick import ahoCorasick
from boyer_moore import boyerMoore


def single(algos, text, pattern):
    # syntax: test([list of algos], text, pattern)

    results = []
    print(f"Text: {text}\nPatt: {pattern}\n")

    for algo in algos:
        print(f"Algo: {algo}")

        if algo == "nai":
            start = timer()
            res = naive(text, pattern)
            end = timer()
            print(f"Time: {end - start:.5f} s")
            print(f"Resu: {res}\n")
            results.append(res)
        elif algo == "kmp":
            start = timer()
            res = knuthMorrisPratt(text, pattern)
            end = timer()
            print(f"Time: {end - start:.5f} s")
            print(f"Resu: {res}\n")
            results.append(res)
        elif algo == "ac":
            start = timer()
            res = ahoCorasick(text, [pattern])
            end = timer()
            print(f"Time: {end - start:.5f} s")
            print(f"Resu: {res}\n")
            results.append(res)
        elif algo == "bm":
            start = timer()
            res = boyerMoore(text, pattern)
            end = timer()
            print(f"Time: {end - start:.5f} s")
            print(f"Resu: {res}\n")
            results.append(res)
        elif algo == "rk":
            start = timer()
            res = rabinKarp(text, pattern)
            end = timer()
            print(f"Time: {end - start:.5f} s")
            print(f"Resu: {res}\n")
            results.append(res)

    return results


def generateRandom(chars=["a", "b", "c", "d"], length=10000, patternLengthRange=(50, 100)):

    # string.printable
    text = "".join(random.choices(chars, k=length))

    patternLenght = random.randrange(
        patternLengthRange[0], patternLengthRange[1])

    patternPos = random.randrange(length-patternLenght)
    pattern = text[patternPos:patternPos+patternLenght]

    return text, pattern, patternPos


if __name__ == "__main__":

    #single(["nai", "kmp", "ac", "bm", "rk"], "blubbluib", "bl")
    text, pattern, firstMatch = generateRandom()
    single(["nai", "kmp", "ac", "bm", "rk"], text, pattern)
