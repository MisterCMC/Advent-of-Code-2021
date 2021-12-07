filename = 'day7_input.txt'
input = open(filename).read()
crabs = input.split(',')
data = []
for crab in crabs:
    data.append(int(crab))

least_fuel = 1000000
for crab in data:
    target = crab
    fuel = 0
    for position in data:
        distance = abs(position - target)
        fuel = fuel + distance
    if fuel < least_fuel:
        least_fuel = int(fuel)
        print(fuel)
