filename  = 'day2_input.txt'
input = open(filename).read()
commands = input.split('\n')
horizontal = 0
depth = 0
aim = 0
for line in commands:
    instruction = line.split(' ')
    if instruction[0] == 'down':
        aim = aim + int(instruction[1])
    elif instruction[0] == 'up':
        aim = aim - int(instruction[1])
    elif instruction[0] == 'forward':
        horizontal = horizontal + int(instruction[1])
        depth = depth + (aim * int(instruction[1]))
score = horizontal * depth
print(score)