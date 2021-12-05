import numpy as np


class Point:
    def __init__(self, point):
        self.x = int(point[0])
        self.y = int(point[1])


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_maximum(self):
        points = [max([self.p1.x, self.p2.x]), max([self.p1.y, self.p2.y])]
        return points

    def get_minimum(self):
        points = [min([self.p1.x, self.p2.x]), min([self.p1.y, self.p2.y])]
        return points


def load_data(filename):
    file = open(filename, 'r')
    lines = []
    min = []
    max = [0, 0]
    for i, file_line in enumerate(file):
        temp = file_line.replace('\n', '').split(' -> ')
        p1 = Point(temp[0].split(','))
        p2 = Point(temp[1].split(','))
        line = Line(p1, p2)
        if line.get_maximum()[0] > max[0]:
            max[0] = line.get_maximum()[0]
        if line.get_maximum()[1] > max[1]:
            max[1] = line.get_maximum()[1]
        if i == 0:
            min = max.copy()
        if line.get_minimum()[0] < min[0]:
            min[0] = line.get_minimum()[0]
        if line.get_minimum()[1] < min[1]:
            min[1] = line.get_minimum()[1]
        lines.append(line)
    print("Finished loading data, lines loaded: {}, min(x,y):{}, max(x,y):{}".format(len(lines), min, max))
    file.close()
    file_data = [lines, min, max]
    return file_data


def get_h_v_lines(line_set):
    h_v_lines = []
    for line in line_set[0]:
        if line.p1.x == line.p2.x or line.p1.y == line.p2.y:
            h_v_lines.append(line)
    return h_v_lines


if __name__ == '__main__':
    lines = load_data('input2')
    h_v_lines = get_h_v_lines(lines)
    shape = [lines[2][0] + 1, lines[2][1] + 1]
    board = np.zeros(shape, dtype=int)
    # Rasterize lines slow algorithm
    for line in h_v_lines:
        if line.p1.x == line.p2.x:  # Vertical line

            v_delta = line.p2.y - line.p1.y
            if v_delta > 0:
                for i in range(0, v_delta + 1):
                    board[line.p1.y + i][line.p1.x] += 1
            else:
                for i in range(v_delta, 1):
                    board[line.p2.y + abs(i)][line.p1.x] += 1
        elif line.p1.y == line.p2.y:  # Horizontal line
            h_delta = line.p2.x - line.p1.x
            if h_delta > 0:
                for i in range(0, h_delta + 1):
                    board[line.p1.y][line.p1.x + i] += 1
            else:
                for i in range(h_delta, 1):
                    board[line.p1.y][line.p2.x + abs(i)] += 1
    print("Number of intersections: %i" % np.count_nonzero(board >= 2))

