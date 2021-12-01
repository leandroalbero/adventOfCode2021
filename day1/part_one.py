if __name__ == '__main__':
    increments = 0
    input_doc = open('input', 'r')
    prev = int(input_doc.readline())
    for line in input_doc:
        if int(line) > prev:
            increments += 1
        prev = int(line)
    print(increments)
