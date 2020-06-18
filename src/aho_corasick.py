import logging
import string
import random

# building the pattern matching machine for the algorithm


def generatePatternMatchingMachine(keywords):

    limitForStates = sum(len(i) for i in keywords)+1
    # goTo is a list of dictonaries, each entries represents one node
    # 0             1               2
    # [{"h":1,"s":3},{"e":2,"i":6}, ....]
    goTo = [dict() for _ in range(limitForStates)]

    # failure is a simple list
    # 1   2  3  4  4
    # [0, 0, 0, 1, ...]
    failure = [0] * limitForStates

    # output is a list of lists
    # 1  2      3  4   5
    # [[],["he"],[],[],["she","he"],...]
    output = [[] for _ in range(limitForStates)]

    # alorithm 1
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

    # algorithm 2
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
    for i in range(limitForStates):
        logging.info(f"State: {i}: {goTo[i]} {failure[i]} {output[i]}")

    return goTo, failure, output


def ahoCorasick(text, keywords):

    goTo, failure, output = generatePatternMatchingMachine(keywords)

    matchList = []

    state = 0
    for i in range(1, len(text)+1):
        while not text[i-1] in goTo[state]:
            state = failure[state]
        state = goTo[state][text[i-1]]

        for match in output[state]:
            matchList.append((i-len(match), match))
            logging.info(f"Found word at {i-len(match)} {match}")

    if not matchList:
        logging.info("No match found")

    return matchList


def generateRandom(chars=["a", "b", "h", "e"], length=100, keywordAmount=3, keywordLengthRange=(2, 7)):

    # string.ascii_uppercase + string.digits would be all characters
    text = "".join(random.choices(chars, k=length))
    keywords = []

    for _ in range(keywordAmount):
        patternLenght = random.randrange(
            keywordLengthRange[0], keywordLengthRange[1])

        patternPos = random.randrange(length-patternLenght)
        keywords.append(text[patternPos:patternPos+patternLenght])

    return text, keywords


if __name__ == "__main__":

    # logging.basicConfig(level=logging.DEBUG)

    print(ahoCorasick("Had I the heavens' embroidered cloths, ", [
          'dear', 'sweetie', 'angel', "dream", "baby"]))
    """
    for i in range(1000):
        text, keywords = generateRandom()
        print(text, keywords)
        print(ahoCorasick(text, keywords))
    """
