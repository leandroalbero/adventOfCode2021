def parse_input(filename):
    file = open(filename, 'r')
    data = []
    for line in file:
        entry = []
        temp = line.replace('\n', '').split(' | ')
        for side in temp:
            entry.append(side.split(' '))
        data.append(entry)
    return data


# find number by len
def find_num(array, num):
    for _number in array:
        if len(_number) == num:
            return _number


def infer_positions(input):
    display = ['', '', '', '', '', '', '']
    seven = find_num(input[0], 3)
    four = find_num(input[0], 4)
    one = find_num(input[0], 2)
    eight = find_num(input[0], 7)
    display[2] = one[0]
    display[5] = one[1]
    display[0] = seven.replace(one[0], '').replace(one[1], '')
    display[1] = four.replace(display[2], '').replace(display[5], '')[0]
    display[3] = four.replace(display[2], '').replace(display[5], '')[1]
    six_seg = find_num(input[0], 6)
    display[6] = \
        six_seg.replace(display[0], '').replace(display[1], '').replace(display[2], '').replace(display[3],
                                                                                                '').replace(
            display[5], '')[0]
    sev_seg = find_num(input[0], 7)
    display[4] = \
        sev_seg.replace(display[0], '').replace(display[1], '').replace(display[2], '').replace(display[3],
                                                                                                '').replace(
            display[5], '').replace(display[6], '')
    return display


def decode(positions, text):
    var = {
        0: [1, 1, 1, 0, 1, 1, 1],
        1: [0, 0, 1, 0, 0, 1, 0],
        2: [1, 0, 1, 1, 1, 0, 1],
        3: [1, 0, 1, 1, 0, 1, 1],
        4: [0, 1, 1, 1, 0, 1, 0],
        5: [1, 1, 0, 1, 0, 1, 1],
        6: [1, 1, 0, 1, 1, 1, 1],
        7: [1, 0, 1, 0, 0, 1, 0],
        8: [1, 1, 1, 1, 1, 1, 1],
        9: [1, 1, 1, 1, 0, 1, 1]
    }
    for i in zip(var.values(), var.keys()):
        for j in range(7):
            i[0][j] = i[0][j] * positions[j]
    for i in zip(var.values(), var.keys()):
        if ''.join(sorted(i[0])) == ''.join(sorted(text)):
            return i[1]
    return 0


if __name__ == '__main__':
    data = parse_input('input3')
    print('Loaded: {} entries'.format(len(data)))
    output_values = []
    for entry in data:
        positions = infer_positions(entry)
        for digit in entry[1]:
            output_values.append(decode(positions, digit))
    print(output_values.count(1)+output_values.count(4)+output_values.count(7)+output_values.count(8))
