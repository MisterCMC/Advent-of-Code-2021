filename = 'day8_input.txt'
input = open(filename).read()
data = input.split('\n')
score = 0
for line in data:
    patterns = line.split('|')
    output = patterns[1].split(' ')
    unique = [2, 3, 4, 7]
    for segment in output:
        if len(segment) in unique:
            score += 1
print(score)