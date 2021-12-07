
f = open("day2.txt", "r")
h = 0
d = 0
for x in f:
  c= x.split()
  if c[0] == 'forward':
      h += int(c[1])
  elif c[0] == 'up':
      d -= int(c[1])
  elif  c[0] == 'down':
      d += int(c[1])

print(d)
print(h)
print(d*h)