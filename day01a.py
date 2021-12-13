count = 0
prev = 0
f = open("day1.txt", "r")
for x in f:
  cur = int(x)
  if cur > prev:
    count += 1
  prev = cur
print(count - 1)