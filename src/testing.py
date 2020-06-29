import random
import matplotlib.pyplot as plt
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


def timeRun(runs=100, chars=["a", "b", "c", "d"], length=10000, patternLengthRange=(50, 100)):

    times = [[] for _ in range(5)]

    for _ in range(runs):

        text, pattern, firstMatch = generateRandom(length=length, chars=chars)

        start = timer()
        res = naive(text, pattern)
        end = timer()
        times[0].append(end - start)

        start = timer()
        res = knuthMorrisPratt(text, pattern)
        end = timer()
        times[1].append(end - start)

        start = timer()
        res = ahoCorasick(text, [pattern])
        end = timer()
        times[2].append(end - start)

        start = timer()
        res = boyerMoore(text, pattern)
        end = timer()
        times[3].append(end - start)

        start = timer()
        res = rabinKarp(text, pattern)
        end = timer()
        times[4].append(end - start)

    return times


if __name__ == "__main__":

    #single(["nai", "kmp", "ac", "bm", "rk"], "blubbluib", "bl")
    #text, pattern, firstMatch = generateRandom()
    #single(["nai", "kmp", "ac", "bm", "rk"], text, pattern)

    fig, (ax1, ax2, ax3) = plt.subplots(3)
    fig.suptitle('Vertically stacked subplots')

    """
    result = timeRun(length=1000)
    ax1.plot(result[0], label="naive")
    ax1.plot(result[1], label="knuth morris pratt")
    ax1.plot(result[2], label="aho Corasick")
    ax1.plot(result[3], label="boyer Moore")
    ax1.plot(result[4], label="rabin Karp")
    # ax1.ylabel('Time')
    ax1.legend()

    result = timeRun(length=10000)
    ax2.plot(result[0], label="naive")
    ax2.plot(result[1], label="knuth morris pratt")
    ax2.plot(result[2], label="aho Corasick")
    ax2.plot(result[3], label="boyer Moore")
    ax2.plot(result[4], label="rabin Karp")
    # ax2.ylabel('Time')
    ax2.legend()

    
    result = timeRun(length=1000000)
    ax3.plot(result[0], label="naive")
    ax3.plot(result[1], label="knuth morris pratt")
    ax3.plot(result[2], label="aho Corasick")
    ax3.plot(result[3], label="boyer Moore")
    ax3.plot(result[4], label="rabin Karp")
    # ax1.ylabel('Time')
    ax3.legend()
    """

    result = timeRun(chars=["0", "1"])
    ax1.plot(result[0], label="naive")
    ax1.plot(result[1], label="knuth morris pratt")
    ax1.plot(result[2], label="aho Corasick")
    ax1.plot(result[3], label="boyer Moore")
    ax1.plot(result[4], label="rabin Karp")
    ax1.set(xlabel="Binary Alphabet")
    ax1.legend()

    result = timeRun(chars=["a", "b", "c", "d"])
    ax2.plot(result[0], label="naive")
    ax2.plot(result[1], label="knuth morris pratt")
    ax2.plot(result[2], label="aho Corasick")
    ax2.plot(result[3], label="boyer Moore")
    ax2.plot(result[4], label="rabin Karp")
    ax2.set(xlabel="4 - Alphabet")
    ax2.legend()

    result = timeRun(chars=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    ax3.plot(result[0], label="naive")
    ax3.plot(result[1], label="knuth morris pratt")
    ax3.plot(result[2], label="aho Corasick")
    ax3.plot(result[3], label="boyer Moore")
    ax3.plot(result[4], label="rabin Karp")
    ax3.set(xlabel="26 Alphabet")
    ax3.legend()

    plt.show()
