filename = 'day7_input.txt'
input = open(filename).read()
crabs = input.split(',')
data = []
for crab in crabs:
    data.append(int(crab))

least_fuel = 100000000000000
for crab in range(0, max(data)):
    target = crab
    fuel = 0
    for position in data:
        distance = abs(position - target)
        cost = sum(range(0, distance+1))
        fuel = fuel + cost
    if fuel < least_fuel:
        least_fuel = int(fuel)
print(least_fuel)