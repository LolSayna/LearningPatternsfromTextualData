
from timeit import default_timer as timer
from knuth_morris_pratt import naive
from knuth_morris_pratt import knuthMorrisPratt
from rabin_karp import rabinKarp
from aho_corasick import ahoCorasick


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

        elif algo == "rk":
            print("skip")
            """
            start = timer()
            res = rabinKarp(text, pattern)
            end = timer()
            print(f"Time: {end - start:.5f} s")
            print(f"Resu: {res}\n")
            results.append(res)
        """
    return results


if __name__ == "__main__":

    print(single(["nai", "kmp", "ac", "rk"], "blubbluib", "bl"))
