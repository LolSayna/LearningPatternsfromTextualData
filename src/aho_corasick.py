import logging
import string


def generatePatternMatchingMachine(keywords):
    # preprocessing function for ac, generates finite state machine

    limitForStates = sum(len(i) for i in keywords)+1

    # goTo is a list of dictonaries, each list entry represents one node and where to go depending on the next charater
    # [{"h":1,"s":3},{"e":2,"i":6}, ....]
    goTo = [dict() for _ in range(limitForStates)]

    # failure is a simple list, each entry represents where to go when no transition is found for each node
    # [0, 0, 0, 1, ...]
    failure = [0] * limitForStates

    # output is a list of lists, it contains all matched keyword for each state
    # [[],["he"],[],[],["she","he"],...]
    output = [[] for _ in range(limitForStates)]

    # alorithm 2 (in the paper)
    newstate = 0
    for a in (keywords):
        state, j = 0, 1
        while j-1 < len(a) and a[j-1] in goTo[state]:
            state = goTo[state][a[j-1]]
            j += 1

        for p in range(j, len(a)+1):
            newstate += 1

            goTo[state][a[p-1]] = newstate
            state = newstate

        output[state].append(a)

    for c in string.printable:
        if not c in goTo[0]:
            goTo[0][c] = 0

    # algorithm 3
    queue = []
    for a, s in goTo[0].items():
        if s != 0:
            queue.append(s)

    while queue:
        r = queue.pop(0)
        for a, s in goTo[r].items():
            queue.append(s)
            state = failure[r]
            while not a in goTo[state]:
                state = failure[state]

            failure[s] = goTo[state][a]
            output[s] = output[s]+output[failure[s]]

    # DEBUG
    if logging.root.level == logging.DEBUG:
        for i in range(limitForStates):
            logging.debug(f"State: {i}: {goTo[i]} {failure[i]} {output[i]}")

    return goTo, failure, output


def ahoCorasick(text, keywords):
    # based on AhoCor.pdf

    goTo, failure, output = generatePatternMatchingMachine(keywords)

    print(goTo, failure, output)
    matchList = []

    state = 0
    for i in range(1, len(text)+1):
        while not text[i-1] in goTo[state]:
            state = failure[state]
        state = goTo[state][text[i-1]]

        for match in output[state]:
            matchList.append((i-len(match), match))

    return matchList


def ahoCorasickSingle(text, keyword):
    # algo that only works on a single keyword to match the format of the other algos
    goTo, failure, output = generatePatternMatchingMachine([keyword])

    matchList = []

    state = 0
    for i in range(1, len(text)+1):
        while not text[i-1] in goTo[state]:
            state = failure[state]
        state = goTo[state][text[i-1]]

        for match in output[state]:
            matchList.append(i-len(match))

    return matchList


if __name__ == "__main__":
    # simple test cases
    # logging.basicConfig(level=logging.DEBUG)

    text, keywords = "he is his she shehshshhehishershehisahshe", [
        "he", "she", "his", "hers"]

    print("Text: ", text)
    print("Pattern: ", keywords)
    print(ahoCorasick(text, keywords))

    text, pattern = "abcbcbcadsdsadasdsadadfgdsgbcb", "bc"
    print(ahoCorasickSingle(text, pattern))
