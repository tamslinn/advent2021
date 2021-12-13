f = open("day7.txt", "r")
crabs = f.readline().split(',')
crabs = list(map(int, crabs))

minFuel = None
bestPos = 0

for pos in range(1,max(crabs)):
    fuel = sum(map(lambda x: sum(range(1,abs(x - pos) + 1)), crabs))
    if minFuel == None:
        minFuel = fuel
    if fuel < minFuel:
        minFuel = fuel
        bestPos = pos

print(bestPos)
print(minFuel)