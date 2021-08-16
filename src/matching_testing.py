import logging
import string
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import wget

import generate

from knuth_morris_pratt import naive
from knuth_morris_pratt import knuthMorrisPratt
from aho_corasick import ahoCorasickSingle
from rabin_karp import rabinKarp
from boyer_moore import boyerMooreFlens
from boyer_moore import boyerMooreLecroq
from boyer_moore import turboBoyerMooreLecroq

algoList = ["naive", "knuthMorrisPratt", "ahoCorasickSingle", "rabinKarp",
            "boyerMooreFlens", "boyerMooreLecroq", "turboBoyerMooreLecroq"]


def run(currentAlgoList, text, pattern):
    # syntax: run([list of algos from algoList], text, pattern)

    results, time = [], []
    logging.info(f"Used algos: {currentAlgoList} Text: {text} Pat: {pattern}")

    for algo in currentAlgoList:

        func = globals()[algo]
        start = timer()
        res = func(text, pattern)
        end = timer()

        results.append(res)
        time.append(end - start)
        logging.info(f"{algo} found {res} in {end - start:.5f} s")

    return results, time


def randomRuns(currentAlgoList=algoList, runs=10, chars=["a", "b", "c", "d"], length=10000, patternLengthRange=(2, 3)):
    # customizible runs function for multiple scenarios

    # for plotting each algo it needs an own list of its times
    times = [[] for _ in range(len(currentAlgoList))]

    for i in range(runs):
        text, pattern, firstMatch = generate.generateRandom(
            length=length, chars=chars, patternLengthRange=patternLengthRange)

        results, time = run(currentAlgoList, text, pattern)

        # check if one of the algos outputed a diffrent result
        if not all(element == results[0] for element in results):
            # if len(set(results)) != 1:
            print(
                f"One of the algos had a different result!\nText: {text}, Pattern: {pattern}\n results:{results}")

        # add the time from each algo in its corresponding list
        for j in range(len(currentAlgoList)):
            times[j].append(time[j])

    return times


def plot(currentAlgoList=algoList, runs=100, chars=["a", "b", "c", "d"], length=10000, patternLengthRange=(5, 10)):

    # logging.basicConfig(level=logging.DEBUG)
    times = randomRuns(currentAlgoList, runs, chars,
                       length, patternLengthRange)

    for i in range(len(currentAlgoList)):
        plt.plot(times[i], label=algoList[i])
        # print(algoList[i], sum(times[i]))

    plt.xlabel("runs")
    plt.ylabel("time")
    plt.legend()
    plt.title("alphabetsize = 4, patternlength = 5-10, length=10000")
    plt.show()


def testShakespeare(pattern, currentAlgoList=algoList, filename="t8.shakespeare.txt"):
    # test for long text files

    text = ""
    r = open(filename, "r")
    for line in r:
        text += line
    r.close()

    # print(len(text))

    print(currentAlgoList)

    print(pattern)
    result, time = run(currentAlgoList, text, pattern)
    print(time)
    print(len(result[0]))


if __name__ == "__main__":

    """
    url = "https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt"
    file = wget.download(url, "Desktop/StringAlgorithms/")
    """
    testShakespeare("the")
    testShakespeare("women")
    testShakespeare("every thing that")
    testShakespeare(
        "lock hanging by it, and borrows money in God's name, the which he")

    # logging.basicConfig(level=logging.DEBUG)
    # print(run(algoList, "cdbcdasdsadasdasdcdbcdasdasdasdcdbcd", "cdbcd"))

    # randomRuns(length=1000, runs=1000, patternLengthRange=(5, 10))

    # ["a","b","c","d"]

    # plot(currentAlgoList=algoList, chars=["a", "b"], runs=100, length=10000,
    #     patternLengthRange=(100, 200))

    """
    Bad case senario for rabin karp


    text = "aaaaaaaaaaaaaaaaaaaaaab"
    pattern = "aaaab"

    results, time = run(["naive", "knuthMorrisPratt", "rabinKarp"],
                        text, pattern)
    print("short")
    print(results)
    for i in time:
        print(f'{i:.6f}')

    text, pattern = "", ""
    for i in range(10000):
        text += "a"
    for i in range(1000):
        pattern += "a"
    text += "b"
    pattern += "b"

    results, time = run(["naive", "knuthMorrisPratt", "rabinKarp"],
                        text, pattern)
    print("long")
    print(results)
    for i in time:
        print(f'{i:.6f}')
    """
