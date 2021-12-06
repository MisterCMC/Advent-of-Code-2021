filename = 'day6_input.txt'
input = open(filename).read()
data = input.split(',')
lanternfish = []
for fish in data:
    lanternfish.append(int(fish))

for i in range(0, 80):
    spawn = 0
    for i in range(0, len(lanternfish)):
        if lanternfish[i] > 0:
            lanternfish[i] = lanternfish[i] - 1
        elif lanternfish[i] == 0:
            lanternfish[i] = 6
            spawn = spawn + 1
    for i in range(0, spawn):
        lanternfish.append(8)
print(len(lanternfish))