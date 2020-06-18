import sys
import string
# https://acm.timus.ru/problem.aspx?space=1&num=1269
# problem with aho_corasick algo


def generatePatternMatchingMachine(keywords):

    limitForStates = sum(len(i) for i in keywords)+1
    goTo = [dict() for _ in range(limitForStates)]
    failure = [0] * limitForStates
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

    return goTo, failure, output


keywords = []
matchList = []
result = []
n = input()

for _ in range(int(n)):
    keywords.append(input())

goTo, failure, output = generatePatternMatchingMachine(keywords)

m = input()
line = 0
for _ in range(int(m)):
    text = input()
    line += 1

    state = 0
    for i in range(1, len(text)+1):
        while not text[i-1] in goTo[state]:
            state = failure[state]
        state = goTo[state][text[i-1]]

        for match in output[state]:
            if not match in matchList:
                matchList.append(match)
                result.append(f"{line} {i-len(match)+1}")

if result == []:
    print("Passed")
else:
    for i in result:
        print(i)
