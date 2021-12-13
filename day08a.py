f = open("day8.txt", "r")

uniq = [2,4,3,7]

count = 0

for x in f:
    parts = x.split('|')
    output = parts[1].split()
    matched = list(filter(lambda x: len(x) in uniq, output))
    count += len(matched)

print(count)