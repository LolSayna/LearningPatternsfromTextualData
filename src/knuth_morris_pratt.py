

def naive(text, pattern):

    patternLenght = len(pattern)
    matchList = []

    for i in range(len(text)-patternLenght+1):

        matches = 0
        while matches < patternLenght and text[i+matches] == pattern[matches]:
            matches += 1

        if matches == patternLenght:

            matchList.append(i)
            print(" " * (i+1), pattern)

    return matchList


def knuthMorrisPratt(text, pattern):
    pass


# simple test cases
if __name__ == "__main__":
    text = "This is a example text with two is."
    pattern = "is"
    atext = "aaaaaaaaab"
    apattern = "aaaab"

    print(f"Testing normal text:\np:{pattern}\nt:{text}")
    print(naive(text, pattern))

    print(f"Testing a text:\np:{apattern}\nt:{atext}")
    print(naive(atext, apattern))
