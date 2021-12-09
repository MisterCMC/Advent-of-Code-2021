import numpy as np
filename = 'day9_input.txt'
input = open(filename).read()
lines = input.split('\n')
matrix = []
for item in lines:
    line = []
    for character in item:
        line.append(int(character))
    matrix.append(line)

score = 0
basin = np.zeros([len(matrix), len(matrix[0])])
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        level = matrix[i][j]
        adjacent = []
        if i < len(matrix)-1:
            adjacent.append(i+1)
            adjacent.append(j)
        if i > 0:
            adjacent.append(i-1)
            adjacent.append(j)
        if j < len(matrix[0])-1:
            adjacent.append(i)
            adjacent.append(j+1)
        if j > 0:
            adjacent.append(i)
            adjacent.append(j-1)
        lowest = True
        for k in range(0, len(adjacent), 2):
            x = adjacent[k]
            y = adjacent[k+1]
            if level >= matrix[x][y]:
                lowest = False
        if lowest == True:
            basin[i][j] = 1
new_score = 0
finished = False
while finished == False:
    old_score = new_score
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if basin[i][j] == 0:
                continue
            level = matrix[i][j]
            adjacent = []
            if i < len(matrix)-1:
                adjacent.append(i+1)
                adjacent.append(j)
            if i > 0:
                adjacent.append(i-1)
                adjacent.append(j)
            if j < len(matrix[0])-1:
                adjacent.append(i)
                adjacent.append(j+1)
            if j > 0:
                adjacent.append(i)
                adjacent.append(j-1)
            for k in range(0, len(adjacent), 2):
                x = adjacent[k]
                y = adjacent[k+1]
                if matrix[x][y] >= level + 1 and matrix[x][y] != 9:
                    basin[x][y] = 1
    new_score = basin.sum()
    if new_score == old_score:
        finished = True

score = []
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        finished = False
        this_score = 0
        adjacent = []
        if basin[i][j] == 0:
            continue
        x = i
        y = j
        adjacent.append(x)
        adjacent.append(y)
        print(x,y)
        while finished == False:
            old_length = len(adjacent)
            if x < len(matrix)-1 and basin[x+1][y] == 1:
                adjacent.append(x+1)
                adjacent.append(y)
            if x > 0 and basin[x-1][y] == 1:
                adjacent.append(x-1)
                adjacent.append(y)
            if y < len(matrix[0])-1 and basin[x][y+1] == 1:
                adjacent.append(x)
                adjacent.append(y+1)
            if y > 0 and basin[x][y-1] == 1:
                adjacent.append(x)
                adjacent.append(y-1)
            new_length = len(adjacent)
            if new_length == 0:
                break
            x = adjacent.pop(0)
            y = adjacent.pop(0)
            if basin[x][y] == 1:
                this_score += 1
                basin[x][y] = 0
            if len(adjacent) == 0:
                finished = True
        print(this_score)
        score.append(this_score)
score.sort()
print(score)
outcome = score[-1] * score[-2] * score[-3]
print(outcome)






