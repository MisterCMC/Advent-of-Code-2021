filename = 'day1_input.txt'
input = open(filename).read()
data_str = input.split('\n')
data = []
score = 0
for depth in data_str:
    data.append(int(depth))
    if len(data) < 4:
        continue
    new_window = data[-1] + data[-2] + data[-3]
    old_window = data[-2] + data[-3] + data[-4]
    if new_window > old_window:
        score = score + 1
print(score)