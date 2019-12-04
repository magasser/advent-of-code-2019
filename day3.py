class Line:
    def __init__(self, xy1, xy2):
        self.x1 = xy1[0]
        self.y1 = xy1[1]
        self.x2 = xy2[0]
        self.y2 = xy2[1]
        if self.x1 == self.x2:
            self.coord = 'y'
        else:
            self.coord = 'x'

    def inersects_with_line_at(self, line):
        if self.coord == line.coord:
            return -1

        if self.coord == 'x':
            if (self.x1 < line.x1 < self.x2 or self.x1 > line.x1 > self.x2) and (line.y1 < self.y1 < line.y2 or line.y1 > self.y1 > line.y2):
                return [line.x1, self.y1]
        else:
            if (self.y1 < line.y1 < self.y2 or self.y1 > line.y1 > self.y2) and (line.x1 < self.x1 < line.x2 or line.x1 > self.x1 > line.x2):
                return [self.x1, line.y1]

        return -1

    def line_string(self):
        return 'x1: ' + str(self.x1) + ', y1: ' + str(self.y1) + ', x2: ' + str(self.x2) + ', y2: ' + str(self.y2)


def travel_path(wire):
    x = 0
    y = 0
    wire_loc = [[x, y]]
    for arg in wire:
        l = arg[0]
        if l == 'R':
            x += int(arg[1:])
        elif l == 'L':
            x -= int(arg[1:])
        elif l == 'U':
            y += int(arg[1:])
        elif l == 'D':
            y -= int(arg[1:])

        wire_loc.append([x,y])

    return wire_loc


def find_intersections(path1, path2):
    intersections = []
    for i in range(len(path1) - 1):
        for k in range(len(path2) - 1):
            line1 = Line([path1[i][0], path1[i][1]], [path1[i+1][0], path1[i+1][1]])
            line2 = Line([path2[k][0], path2[k][1]], [path2[k+1][0], path2[k+1][1]])
            intersection = line1.inersects_with_line_at(line2)
            if intersection != -1:
                intersections.append(intersection)
    return intersections


def shortest_manhatten_distance(ints):
    min = abs(ints[0][0]) + abs(ints[0][1])

    for i in ints:
        md = abs(i[0]) + abs(i[1])
        if md < min:
            min = md

    return min


def steps_to_intersection(p, i):
    steps = 0
    for k in range(len(p) - 1):
        coord = ''
        if p[k][0] == p[k+1][0]:
            coord = 'y'
        else:
            coord = 'x'

        if coord == 'x':
            if (p[k][0] < i[0] < p[k+1][0] or p[k][0] > i[0] > p[k+1][0]) and p[k][1] == i[1]:
                steps += abs(p[k][0] - i[0])
                break
        else:
            if (p[k][1] < i[1] < p[k + 1][1] or p[k][1] > i[1] > p[k + 1][1]) and p[k][0] == i[0]:
                steps += abs(p[k][1] - i[1])
                break
        steps += abs(p[k][0] - p[k+1][0]) + abs(p[k][1] - p[k+1][1])

    return steps


def fewest_steps_to_intersection(p1, p2, ints):
    min_steps = 9999999999
    for i in ints:
        steps = steps_to_intersection(p1, i) + steps_to_intersection(p2, i)
        if steps < min_steps:
            min_steps = steps

    return min_steps


with open('day3_data/wire1.txt', 'r') as wire1_txt:
    wire1 = wire1_txt.read().split(',')

with open('day3_data/wire2.txt', 'r') as wire2_txt:
    wire2 = wire2_txt.read().split(',')

#wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
#wire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
path1 = travel_path(wire1)
path2 = travel_path(wire2)
intersections = find_intersections(path1, path2)
f_steps = fewest_steps_to_intersection(path1, path2, intersections)
m_distance = shortest_manhatten_distance(intersections)

print(m_distance)
print(f_steps)