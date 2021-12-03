filename = 'day3_input.txt'
input = open(filename).read()
data = input.split('\n')
oxygen = list(data)
co2 = list(data)
for i in range(0, 12):
    sum = 0
    most_common = '1'
    total = len(oxygen)
    for code in oxygen:
        sum = sum + int(code[i])
    mean = sum / total
    if mean > 0.5:
        most_common = '1'
    elif mean < 0.5:
        most_common = '0'
    for j in range(0, len(oxygen)):
        if oxygen[j][i] == most_common:
            continue
        elif oxygen[j][i] != most_common:
            oxygen[j] = None
    oxygen = list(filter(None, oxygen))
    if len(oxygen) == 1:
        print(oxygen)
        break

for i in range(0, 12):
    sum = 0
    most_common = '1'
    total = len(co2)
    for code in co2:
        sum = sum + int(code[i])
    mean = sum / total
    if mean > 0.5:
        most_common = '1'
    elif mean < 0.5:
        most_common = '0'

    for j in range(0, len(co2)):
        if co2[j][i] != most_common:
            continue
        elif co2[j][i] == most_common:
            co2[j] = None
    co2 = list(filter(None, co2))
    if len(co2) == 1:
        print(co2)
        break

score = int(co2[0], 2) * int(oxygen[0], 2)
print(score)