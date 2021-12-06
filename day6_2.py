filename = 'day6_input.txt'
input = open(filename).read()
data = input.split(',')
lanternfish = [0,0,0,0,0,0,0,0,0]
for fish in data:
    if int(fish) == 0:
        lanternfish[0] = lanternfish[0]+1
    if int(fish) == 1:
        lanternfish[1] = lanternfish[1]+1
    if int(fish) == 2:
        lanternfish[2] = lanternfish[2]+1
    if int(fish) == 3:
        lanternfish[3] = lanternfish[3]+1
    if int(fish) == 4:
        lanternfish[4] = lanternfish[4]+1
    if int(fish) == 5:
        lanternfish[5] = lanternfish[5]+1
    if int(fish) == 6:
        lanternfish[6] = lanternfish[6]+1
    if int(fish) == 7:
        lanternfish[7] = lanternfish[7]+1
    if int(fish) == 8:
        lanternfish[8] = lanternfish[8]+1

for i in range(0, 256):
    updating = [0,0,0,0,0,0,0,0,0]
    updating[8] = lanternfish[0]
    updating[7] = lanternfish[8]
    updating[6] = lanternfish[7] + lanternfish[0]
    updating[5] = lanternfish[6]
    updating[4] = lanternfish[5]
    updating[3] = lanternfish[4]
    updating[2] = lanternfish[3]
    updating[1] = lanternfish[2]
    updating[0] = lanternfish[1]
    lanternfish = list(updating)

population = 0
for age in lanternfish:
    population = population + age

print(population)
