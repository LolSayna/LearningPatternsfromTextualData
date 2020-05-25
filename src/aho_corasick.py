
import string


def generatePatternMatchingMachine(keywords):

    limitForStates = sum(len(i) for i in keywords)

    # goTo is a list of dictonaries, each entries represents one node
    # 0             1               2
    # [{"h":1,"s":3},{"e":2,"i":6}, ....]
    goTo = [dict() for _ in range(limitForStates)]

    # failure is a simple list
    # 1   2  3  4  4
    # [0, 0, 0, 1, ...]
    failure = []

    # output is a list of lists
    # 1  2      3  4   5
    # [[],["he"],[],[],["she","he"],...]
    output = [[] for _ in range(limitForStates)]

    # alorithm 1
    newstate = 0
    for a in (keywords):

        state, j = 0, 1
        while a[j-1] in goTo[state]:
            state = goTo[state][a[j-1]]
            j += 1

        for p in range(j, len(a)):
            newstate += 1

            goTo[state][a[p-1]] = newstate
            state = newstate

        output[state].append(a)

    for c in string.ascii_letters + string.digits + " ":
        goTo[0][c] = 0

    # for i in range(limitForStates):
    #    print(f"{i}: {goTo[i]} {output[i]}")

    # algorithm 2
    queue = []
    for a, s in goTo[0].items():
        print(a, s)

    return goTo, failure, output


def ahoCorastick(text, keywords):

    goTo, failure, output = generatePatternMatchingMachine(keywords)

    return None


if __name__ == "__main__":

    ahoCorastick("abc", ["he", "she", "his", "hers"])
