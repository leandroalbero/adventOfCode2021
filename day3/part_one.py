import numpy as np

if __name__ == '__main__':
    input_doc = open('input', 'r')
    data = []
    for line in input_doc:
        data.append((line.replace('\n', '')))
    sums = np.zeros(len(data[0]), dtype=int)
    for row in data:
        pos = 0
        for col in row:
            sums[pos] += int(col)
            pos += 1
    gamma = np.zeros(len(data[0]), dtype=int)
    epsilon = np.zeros(len(data[0]), dtype=int)
    pos = 0
    for row in sums:
        if row > len(data)/2:
            gamma[pos] = 1
            epsilon[pos] = 0
        else:
            gamma[pos] = 0
            epsilon[pos] = 1
        pos += 1

    print(gamma)  # 2663
    print(epsilon)  # 1432
    print(2663*1432)
