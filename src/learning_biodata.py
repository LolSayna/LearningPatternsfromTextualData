import os
from learning_Patterns import descPat
from learning_Util import *



def getBioData(name):
    # returns a list of int arrays

    path = "src/data/first_sample_bio"
    # old path way
    #path = os.getcwd()+"\src\patterns\data\Allocreadiata\IcavJvXFav.fasta"
    #path = os.getcwd()+"\src\patterns\data\Filobasidium\yyhZkgalXA.fasta"
    #path = os.getcwd()+"\src\patterns\data\Holtermaniella\lpFGRo1oWR.fasta"
    #path = os.getcwd()+"\src\patterns\data\Tremella\1nFa7vRp7o.fasta"

    # works on my windows pc
    path = os.getcwd() + "\src\patterns\data\\" + name
    for e in os.walk(path):
        filename = e[2][0]
    fullPath = path + "\\" + filename
    #print(fullPath)


    with open(fullPath) as f:
        s = f.read()

    sample = []
    for line in s.splitlines():

        if line[0] == ">":
            pass
        else:
            sample.append(line.lower())

    # here we have an array of strings now, with lower case a,c,g,t
    #print(sample)

    # next convert into usable intArrays
    intSample = []
    for line in sample:
        intLine = []
        for c in line:
            
            """
            # to use a,b,c,d
            if c == "a":
                intLine.append(1)
            elif c == "c":
                intLine.append(3)
            elif c == "g":
                intLine.append(5)
            elif c == "t":
                intLine.append(7)
            else:
                print("unsupported input")
            """

            # get the number of the char in alphabet and make it uneven, so it fits in the structure
            intLine.append((ord(c) - ord("a")) * 2 + 1)

        intSample.append(intLine)

    return intSample

nameList = ["Allocreadiata", "Filobasidium", "Holtermaniella", "Tremella"]

for name in nameList:
    #name = "Allocreadiata"

    sample = getBioData(name)
    pat = descPat(sample)

    print(name)
    print(convertToAlphabet(pat))
    """
    with open(name+".txt", "w") as results:
        results.write(convertToAlphabet(pat) + "\n\n\n")

        for subSample in sample:
            results.write(convertToAlphabet(subSample) + "\n")
    """