import random
import string


def generateRandom(chars=["a", "b", "c", "d"], length=10000, patternLengthRange=(50, 100)):

    # string.printable for all standard chars
    text = "".join(random.choices(chars, k=length))

    patternLenght = random.randrange(
        patternLengthRange[0], patternLengthRange[1])

    patternPos = random.randrange(length-patternLenght)
    pattern = text[patternPos:patternPos+patternLenght]

    return text, pattern, patternPos

   
"""
    english text als input data

    https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt
"""


def generateRegularPattern(length, varCount):
    # generates a random regular pattern of length with varCount number of Variables, returns in string form

    pattern = random.choices(string.ascii_lowercase, k=length)

    varPos = random.sample(range(length), varCount)

    for i, varPos in enumerate(sorted(varPos)):
        pattern[varPos] = chr(ord("A") + i)

    return "".join(pattern)



def generateWordsFromPattern(pattern, wordCount, replaceMin, replaceMax):
    # takes the pattern and generates a random string to replace each variable, the lenght of the string is in replaceRange; does that for wordCount words 

    words = []
    for _ in range(wordCount):

        word = ""
        for c in pattern:
            if c.isupper():
                for _ in range(random.randint(replaceMin, replaceMax)):
                    word += random.choice(string.ascii_lowercase)
            else:
                word += c
        words.append(word)
    
    return words



if __name__ == "__main__":
    
    print(generateRegularPattern(20,1))
    
    print(generateWordsFromPattern("qAbxBfCDxsmEqsefbmvy", 5, 1,3))