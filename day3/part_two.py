import math


def calc_oxy(numbers, depth):
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 2:
        if int(numbers[0][depth]) == 1:
            return numbers[0]
        else:
            return numbers[1]
    sum2 = 0
    most_common = 0
    new_numbers = []
    for row2 in numbers:
        sum2 += int(row2[depth])
    if sum2 >= math.ceil(len(numbers) / 2):
        most_common = 1
    for row2 in numbers:
        if most_common == int(row2[depth]):
            new_numbers.append(row2)
    return calc_oxy(new_numbers, depth + 1)


def calc_co2(numbers, depth):
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 2:
        if int(numbers[0][depth]) == 0:
            return numbers[0]
        else:
            return numbers[1]
    sum2 = 0
    most_common = 0
    new_numbers = []
    for row in numbers:
        sum2 += int(row[depth])
    if sum2 >= math.ceil(len(numbers) / 2):
        most_common = 1
    for row in numbers:
        if most_common != int(row[depth]):
            new_numbers.append(row)
    return calc_co2(new_numbers, depth + 1)


if __name__ == '__main__':
    input_doc = open('input', 'r')
    data = []
    for line in input_doc:
        data.append((line.replace('\n', '')))
    oxygen = calc_oxy(data, 0)
    co2 = calc_co2(data, 0)
    print("oxygen: " + oxygen)  # 2526
    print("co2: " + co2)  # 1184
    # result 2990784
