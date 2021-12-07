import statistics

f = open("day7.txt", "r")
crabs = f.readline().split(',')
crabs = list(map(int, crabs))

middle = statistics.median(crabs)

fuel = sum(map(lambda x: abs(x - middle), crabs))
print(fuel)