
f = open("day2.txt", "r")
a = 0
h = 0
d = 0
for x in f:
  c= x.split()
  if c[0] == 'forward':
      h += int(c[1])
      d += int(c[1]) * a
  elif c[0] == 'up':
      a -= int(c[1])
  elif  c[0] == 'down':
      a += int(c[1])

print(d)
print(h)
print(d*h)