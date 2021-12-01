filename = 'day1_input.txt'
input = open(filename).read()
data_str = input.split('\n')
data = []
score = 0
for depth in data_str:
    data.append(int(depth))
    if len(data) == 1:
        continue
    if data[-1] > data[-2]:
        score = score + 1
print(score)
