filename  = 'day2_input.txt'
input = open(filename).read()
commands = input.split('\n')
horizontal = 0
depth = 0
for line in commands:
    instruction = line.split(' ')
    if instruction[0] == 'forward':
        horizontal = horizontal + int(instruction[1])
    elif instruction[0] == 'down':
        depth = depth + int(instruction[1])
    elif instruction[0] == 'up':
        depth = depth - int(instruction[1])
score = horizontal * depth
print(score)