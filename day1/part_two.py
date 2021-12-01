if __name__ == '__main__':
    increments = 0
    input_doc = open('input', 'r')
    doc = []
    for line in input_doc:
        doc.append(int(line))
    posA = 0
    posB = 1
    posC = 2

    while posA < (len(doc) - 3):
        A = doc[posA] + doc[posB] + doc[posC]
        B = doc[posA + 1] + doc[posB + 1] + doc[posC + 1]
        if B > A:
            increments += 1
        posA += 1
        posB += 1
        posC += 1
    print(increments)
