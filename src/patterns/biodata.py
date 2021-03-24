from patternLanguage import descPat


def transformInput():

    path = "/home/daubuntu/Desktop/StringAlgorithms/src/patterns/data/Holtermaniella/lpFGRo1oWR.fasta"

    with open(path) as f:
        s = f.read()

    sample = []
    for line in s.splitlines():

        if line[0] == ">":
            pass
            # print("a", line)
        else:
            # print("b", line)
            sample.append(line[:30])

    print(sample)
    print(descPat(sample))


transformInput()

sample = ["GTGAACAACCTCAACCTTGA", "GTGAACAACCTCAACCTTGA"]
print(descPat(sample))