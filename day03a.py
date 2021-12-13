
f = open("day3.txt", "r")
agg = [0,0,0,0,0,0,0,0,0,0,0,0]
lines = 0
for x in f:
    lines += 1
    for i in range(0, 12):
        agg[i] += int(x[i])
print(agg)

gamma = ""
epsilon = ""
for i in range(0, 12):
    if agg[i] > lines/2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
print(gamma)
gamma = int(gamma, base=2)
epsilon = int(epsilon, base=2)

print(gamma* epsilon)