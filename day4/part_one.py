import numpy as np
import numpy.linalg

# # CAREFUL: This solution works but is not valid because it uses the Determinant of the matrix which also counts
# diagonals, part_two uses a 'correct' method by checking only rows and columns.
if __name__ == '__main__':
    file = open('input', 'r')
    draws = file.readline().replace('\n', '').split(',')
    file.readline()
    bingo = np.zeros((5, 5), dtype=int)
    row = 0
    bingos = []
    for line in file:
        if line == '\n':
            bingos.append(bingo)
            bingo = np.zeros((5, 5), dtype=int)
            row = 0
        else:
            temp = line.replace('\n', '').replace('  ', ' ').split(' ')
            int_temp = []
            for number in temp:
                if number == '':
                    continue
                int_temp.append(int(number))
            bingo[row] = int_temp
            row += 1
    bingos.append(bingo)
    boards_won = 0
    for number in draws:
        print("Checking number: " + number)
        for i, bingo in enumerate(bingos):
            test = np.where(bingo == int(number))
            if len(test[0]) == 0:
                continue
            bingos[i][test[0][0]][test[1][0]] = 0
            if numpy.linalg.det(bingo) == 0:
                print("Bingo")
                boards_won += 1
                print(np.sum(bingo) * int(number))
                bingos[i] = None
    print(boards_won)
