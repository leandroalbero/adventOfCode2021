if __name__ == '__main__':
    input_doc = open('input', 'r')
    h_pos = 0
    depth = 0
    aim = 0

    doc = []
    for line in input_doc:
        doc.append(line.replace('\n', '').split(' '))
    for line in doc:
        value = int(line[1])
        if line[0] == 'forward':
            h_pos += value
            depth += aim * value
        elif line[0] == 'down':
            aim += value
        else:
            aim -= value
    print(h_pos * depth)
