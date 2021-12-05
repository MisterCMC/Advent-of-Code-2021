import numpy as np
filename = 'day5_input.txt'
input = open(filename).read()
instructions = input.split('\n')

def generate_line(x1, x2, y1, y2):
    coordinates = []
    if x1 == x2 and y2 > y1:
        for i in range(y1, y2+1, 1):
            n = str(i).zfill(3)
            x = str(x1).zfill(3)
            position = x+n
            coordinates.append(position)
    elif x1 == x2 and y2 < y1:
        for i in range(y1, y2-1, -1):
            n = str(i).zfill(3)
            x = str(x1).zfill(3)
            position = x+n
            coordinates.append(position)
    elif y1 == y2 and x2 > x1:
        for i in range(x1, x2+1, 1):
            n = str(i).zfill(3)
            y = str(y1).zfill(3)
            position = n + y
            coordinates.append(position)
    elif y1 == y2 and x2 < x1:
        for i in range(x1, x2-1, -1):
            n = str(i).zfill(3)
            y = str(y1).zfill(3)
            position = n + y
            coordinates.append(position)
    return coordinates

danger = set()
doubled = set()
score = 0
for i in range(0, len(instructions)):
    coordinates = instructions[i].split(' -> ')
    start = coordinates[0].split(',')
    end = coordinates[1].split(',')
    x1 = int(start[0])
    y1 = int(start[1])
    x2 = int(end[0])
    y2 = int(end[1])
    if x1 != x2 and y1 != y2:
        continue
    line = set(generate_line(x1, x2, y1, y2))
    multiples = danger.intersection(line)
    cross = multiples.difference(doubled)
    danger.update(line)
    doubled.update(multiples)
    score = score + len(cross)
    line.clear()
    cross.clear()
print(score)
