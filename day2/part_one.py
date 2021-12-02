if __name__ == '__main__':
    input_doc = open('input', 'r')
    h_pos = 0
    depth = 0
    doc = []
    for line in input_doc:
        doc.append(line.replace('\n', '').split(' '))
    for line in doc:
        if line[0] == 'forward':
            h_pos += int(line[1])
        elif line[0] == 'down':
            depth += int(line[1])
        else:
            depth -= int(line[1])
    print(h_pos * depth)
