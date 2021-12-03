filename = 'day3_input.txt'
input = open(filename).read()
data = input.split('\n')
gamma = []
epsilon = []
for i in range(0, 12):
    sum = 0
    for code in data:
        sum = sum + int(code[i])
    if sum > 500:
        gamma.append(1)
        epsilon.append(0)
    elif sum < 500:
        gamma.append(0)
        epsilon.append(1)

gamma_bin  = int("".join(str(i) for i in gamma),2)
epsilon_bin = int("".join(str(i) for i in epsilon),2)
score = gamma_bin * epsilon_bin
print(score)