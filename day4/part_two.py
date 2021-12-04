import numpy as np


def check_rows(table):
    for row2 in table:
        if np.sum(row2) == 0:
            return True
    return False


def check_cols(table):
    new_table = table.T
    for col in new_table:
        if np.sum(col) == 0:
            return True
    return False


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
            if int(number) == 12:
                print()
            test = np.where(bingo == int(number))
            if len(test[0]) == 0:
                continue
            bingos[i][test[0][0]][test[1][0]] = 0
            if check_rows(bingo) or check_cols(bingo):
                print("BINGO! on board: "+str(i))
                print(bingo)
                boards_won += 1
                print(np.sum(bingo) * int(number))
                bingos[i] = None
        if boards_won == len(bingos):
            print("game finished")
            break
