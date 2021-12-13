
f = open("day1.txt", "r")
strings = f.read().splitlines()
ints = list(map(lambda x: int(x), strings))

count = 0
prev = 0
for x in range(0, len(ints)-2):
  cur = ints[x]+ints[x+1]+ints[x+2]
  if cur > prev:
    count += 1
  prev = cur
print(count-1)