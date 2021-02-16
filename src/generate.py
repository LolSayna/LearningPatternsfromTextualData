import random
import string


def generateRandom(
    chars=["a", "b", "c", "d"], length=10000, patternLengthRange=(50, 100)
):

    # string.printable for all standard chars
    text = "".join(random.choices(chars, k=length))

    patternLenght = random.randrange(patternLengthRange[0], patternLengthRange[1])

    patternPos = random.randrange(length - patternLenght)
    pattern = text[patternPos : patternPos + patternLenght]

    return text, pattern, patternPos


"""
    english text als input data

    https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt
"""
