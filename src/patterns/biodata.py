from patternLanguage import descPat

# needed since there can only be 25 variables at the same time
maxLength = 25


def transformInput():

    path = "/home/daubuntu/Desktop/StringAlgorithms/src/patterns/data/Holtermaniella/lpFGRo1oWR.fasta"

    with open(path) as f:
        s = f.read()

    # workarround for now
    sample = [[] for i in range(100)]

    for line in s.splitlines():

        if line[0] == ">":
            pass
        else:

            # care with block size
            for i in range((len(line) // maxLength) + 1):
                sample[i].append((line[i * maxLength : (i + 1) * maxLength]).lower())

    # print(sample)
    for subsample in sample:
        if subsample:
            print(subsample)
            print(descPat(subsample))


transformInput()

# sample = ["GTGAACAACCTCAACCTTGA", "GTGAACAACCTCAACCTTGA"]
# print(descPat(sample))
