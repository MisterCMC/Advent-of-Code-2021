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
            risk = level + 1
            score += risk
print(score)





