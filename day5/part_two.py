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

    def leftmost_up(self):
        if self.p1.x < self.p2.x:
            return [self.p1, self.p2]
        elif self.p1.x > self.p2.x:
            return [self.p2, self.p1]
        else:
            if self.p1.y > self.p2.y:
                return [self.p2, self.p1]
            else:
                return [self.p1, self.p2]

    def is_vertical(self):
        if self.p1.x == self.p2.x:
            return True
        else:
            return False

    def is_horizontal(self):
        if self.p1.y == self.p2.y:
            return True
        else:
            return False

    def is_diagonal(self):
        if not self.is_horizontal() and not self.is_vertical():
            return True
        else:
            return False


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
    lines = load_data('input')
    h_v_lines = get_h_v_lines(lines)
    shape = [lines[2][0] + 1, lines[2][1] + 1]
    board = np.zeros(shape, dtype=int)
    # Rasterize lines divided differences
    for line in lines[0]:
        ordered_line = line.leftmost_up()
        if line.is_horizontal():
            print("- [{},{}] -> [{},{}]".format(line.p1.x, line.p1.y, line.p2.x, line.p2.y))
            for i in range(ordered_line[0].x, ordered_line[1].x + 1):
                board[i][ordered_line[0].y] += 1
        elif line.is_vertical():
            print("| [{},{}] -> [{},{}]".format(line.p1.x, line.p1.y, line.p2.x, line.p2.y))
            for i in range(ordered_line[0].y, ordered_line[1].y + 1):
                board[ordered_line[0].x][i] += 1
        else:
            print("/ [{},{}] -> [{},{}]".format(line.p1.x, line.p1.y, line.p2.x, line.p2.y))
            for i in range(ordered_line[0].x, ordered_line[1].x + 1):
                m = (ordered_line[1].y - ordered_line[0].y) / (ordered_line[1].x - ordered_line[0].x)
                y = m * (i - ordered_line[0].x) + ordered_line[0].y
                board[i][int(y)] += 1

    print("Number of intersections: %i" % np.count_nonzero(board >= 2))
