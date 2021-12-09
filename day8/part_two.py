# NON WORKING

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
    found = []
    for _number in array:
        if len(_number) == num:
            found.append(_number)
    return found


def infer_positions(input):
    display = ['', '', '', '', '', '', '']
    seven = find_num(input[0], 3)
    number_four = find_num(input[0], 4)
    number_one = find_num(input[0], 2)
    number_eight = find_num(input[0], 7)
    number_nine = find_num(input[0], 6)

    display[2] = number_one[0][1]
    display[5] = number_one[0][0]
    display[0] = seven[0].replace(number_one[0][0], '').replace(number_one[0][1], '')
    # cfbegad - cbdgef
    number_eight = number_eight[0].replace(display[2], '').replace(display[5], '').replace(display[0], '')
    for text in number_nine:
        temp = number_eight
        for character in text:
            temp = temp.replace(character, '')
        if len(temp) == 1:
            number_eight = temp
            break
    display[4] = number_eight
    display[1] = number_four[0].replace(display[2], '').replace(display[5], '').replace(display[0], '').replace(display[4],'')[0]
    display[3] = number_four[0].replace(display[2], '').replace(display[5], '').replace(display[0], '').replace(display[4],'').replace(display[1],'')
    number_eight = find_num(input[0], 7)[0]
    display[6] = number_eight.replace(display[0], '').replace(display[1], '').replace(display[2], '').replace(
        display[3], '').replace(display[4], '').replace(display[5], '')
    for i in display:
        if i == '':
            print("ERROR")
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
    data = parse_input('input2')
    print('Loaded: {} entries'.format(len(data)))
    for entry in data:
        output_values = []
        positions = infer_positions(entry)
        for digit in entry[1]:
            output_values.append(decode(positions, digit))
        print(output_values)
        # print(output_values.count(1)+output_values.count(4)+output_values.count(7)+output_values.count(8))
    exit(0)
