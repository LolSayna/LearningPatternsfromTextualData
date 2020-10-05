import logging
import string
import matplotlib.pyplot as plt
from timeit import default_timer as timer

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

# TODO: different results happens


def plot(runs=100, chars=["a", "b", "c", "d"], length=10000, patternLengthRange=(5, 10)):

    times = randomRuns(algoList, runs, chars,
                       length, patternLengthRange)

    for i in range(len(algoList)):
        plt.plot(times[i], label=algoList[i])

    plt.xlabel("runs")
    plt.ylabel("time")
    plt.legend()
    plt.show()


if __name__ == "__main__":

    # logging.basicConfig(level=logging.INFO)
    #print(run(algoList, "abdsdbsdbbds", "db"))

    # print(randomRuns(runs=20))

    plot(patternLengthRange=(10, 20))
