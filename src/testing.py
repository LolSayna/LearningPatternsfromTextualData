import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from knuth_morris_pratt import naive
from knuth_morris_pratt import knuthMorrisPratt
from rabin_karp import rabinKarp
from aho_corasick import ahoCorasick
from boyer_moore import boyerMooreLecroq
from boyer_moore import turboBoyerMooreLecroq
from boyer_moore import boyerMooreFlens


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
            res = boyerMooreFlens(text, pattern)
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
        elif algo == "tbm":
            start = timer()
            res = turboBoyerMooreLecroq(text, pattern)
            end = timer()
            print(f"Time: {end - start:.5f} s")
            print(f"Resu: {res}\n")
            results.append(res)

    return results


# testing if diffrent algorithms lead to diffrent results
def compareResults(times=100):

    for i in range(times):
        text, pattern, pos = generateRandom(length=1000)
        if naive(text, pattern) != knuthMorrisPratt(text, pattern):
            print(print(f"p:{pattern}\nt:{text}"))
            n = naive(text, pattern)
            print(len(n), n)
            k = knuthMorrisPratt(text, pattern)
            print(len(k), k)


def generateRandom(chars=["a", "b", "c", "d"], length=10000, patternLengthRange=(50, 100)):

    # string.printable for all standard chars
    text = "".join(random.choices(chars, k=length))

    patternLenght = random.randrange(
        patternLengthRange[0], patternLengthRange[1])

    patternPos = random.randrange(length-patternLenght)
    pattern = text[patternPos:patternPos+patternLenght]

    return text, pattern, patternPos


def timeRun(runs=100, chars=["a", "b", "c", "d"], length=10000, patternLengthRange=(50, 100)):

    times = [[] for _ in range(7)]

    for _ in range(runs):

        text, pattern, firstMatch = generateRandom(
            length=length, chars=chars, patternLengthRange=patternLengthRange)

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
        res = boyerMooreFlens(text, pattern)
        end = timer()
        times[3].append(end - start)

        start = timer()
        res = rabinKarp(text, pattern)
        end = timer()
        times[4].append(end - start)

        start = timer()
        res = turboBoyerMooreLecroq(text, pattern)
        end = timer()
        times[5].append(end - start)

        start = timer()
        res = boyerMooreLecroq(text, pattern)
        end = timer()
        times[6].append(end - start)

    return times


if __name__ == "__main__":

    #single(["nai", "kmp", "ac", "bm", "rk", "tbm"], "blubbluib", "bl")
    #text, pattern, firstMatch = generateRandom()
    #single(["nai", "kmp", "ac", "bm", "rk", "tbm"], text, pattern)

    fig, (ax1, ax2, ax3) = plt.subplots(3)
    fig.suptitle('Vertically stacked subplots')
    """
    result = timeRun(length=100)
    ax1.plot(result[0], label="naive")
    ax1.plot(result[1], label="knuth morris pratt")
    ax1.plot(result[2], label="aho Corasick")
    ax1.plot(result[3], label="boyer Moore flens")
    ax1.plot(result[4], label="rabin Karp")
    ax1.plot(result[5], label="turbo Boyer Moore")
    ax1.plot(result[6], label="boyer Moore lecroq")
    ax1.set(xlabel="1000 legnth text")
    ax1.legend()

    result = timeRun(length=1000)
    ax2.plot(result[0], label="naive")
    ax2.plot(result[1], label="knuth morris pratt")
    ax2.plot(result[2], label="aho Corasick")
    ax2.plot(result[3], label="boyer Moore flens")
    ax2.plot(result[4], label="rabin Karp")
    ax2.plot(result[5], label="turbo Boyer Moore")
    ax2.plot(result[6], label="boyer Moore lecroq")
    ax2.set(xlabel="10000 legnth text")
    ax2.legend()

    result = timeRun(length=10000)
    ax3.plot(result[0], label="naive")
    ax3.plot(result[1], label="knuth morris pratt")
    ax3.plot(result[2], label="aho Corasick")
    ax3.plot(result[3], label="boyer Moore flens")
    ax3.plot(result[4], label="rabin Karp")
    ax3.plot(result[5], label="turbo Boyer Moore")
    ax3.plot(result[6], label="boyer Moore lecroq")
    ax3.set(xlabel="100000 legnth text")
    ax3.legend()
    """
    """
    result = timeRun(chars=["0", "1"])
    ax1.plot(result[0], label="naive")
    ax1.plot(result[1], label="knuth morris pratt")
    ax1.plot(result[2], label="aho Corasick")
    ax1.plot(result[3], label="boyer Moore flens")
    ax1.plot(result[4], label="rabin Karp")
    ax1.plot(result[5], label="turbo Boyer Moore")
    ax1.plot(result[6], label="boyer Moore lecroq")
    ax1.set(xlabel="Binary Alphabet")
    ax1.legend()

    result = timeRun(chars=["a", "b", "c", "d"])
    ax2.plot(result[0], label="naive")
    ax2.plot(result[1], label="knuth morris pratt")
    ax2.plot(result[2], label="aho Corasick")
    ax2.plot(result[3], label="boyer Moore flens")
    ax2.plot(result[4], label="rabin Karp")
    ax2.plot(result[5], label="turbo Boyer Moore")
    ax2.plot(result[6], label="boyer Moore lecroq")
    ax2.set(xlabel="4 - Alphabet")
    ax2.legend()

    result = timeRun(chars=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    ax3.plot(result[0], label="naive")
    ax3.plot(result[1], label="knuth morris pratt")
    ax3.plot(result[2], label="aho Corasick")
    ax3.plot(result[3], label="boyer Moore flens")
    ax3.plot(result[4], label="rabin Karp")
    ax3.plot(result[5], label="turbo Boyer Moore")
    ax3.plot(result[6], label="boyer Moore lecroq")
    ax3.set(xlabel="26 Alphabet")
    ax3.legend()

    """
    result = timeRun(patternLengthRange=(1, 2), chars=["0", "1"])
    ax1.plot(result[0], label="naive")
    ax1.plot(result[1], label="knuth morris pratt")
    ax1.plot(result[2], label="aho Corasick")
    ax1.plot(result[3], label="boyer Moore flens")
    ax1.plot(result[4], label="rabin Karp")
    ax1.plot(result[5], label="turbo Boyer Moore")
    ax1.plot(result[6], label="boyer Moore lecroq")
    ax1.set(xlabel="Short Pattern")
    ax1.legend()

    result = timeRun(patternLengthRange=(500, 750), chars=["0", "1"])
    ax2.plot(result[0], label="naive")
    ax2.plot(result[1], label="knuth morris pratt")
    ax2.plot(result[2], label="aho Corasick")
    ax2.plot(result[3], label="boyer Moore flens")
    ax2.plot(result[4], label="rabin Karp")
    ax2.plot(result[5], label="turbo Boyer Moore")
    ax2.plot(result[6], label="boyer Moore lecroq")
    ax2.set(xlabel="Long Pattern")
    ax2.legend()

    result = timeRun(patternLengthRange=(0, 1000), chars=["0", "1"])
    ax3.plot(result[0], label="naive")
    ax3.plot(result[1], label="knuth morris pratt")
    ax3.plot(result[2], label="aho Corasick")
    ax3.plot(result[3], label="boyer Moore flens")
    ax3.plot(result[4], label="rabin Karp")
    ax3.plot(result[5], label="turbo Boyer Moore")
    ax3.plot(result[6], label="boyer Moore lecroq")
    ax3.set(xlabel="Wide range Pattern")
    ax3.legend()

    plt.show()
