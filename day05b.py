import re
from functools import reduce
f = open("day5.txt")


vents = []

maxX = 0
maxY = 0

for row in f:
  vent = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", row).groups()
  vent = [int(vent[0]),int(vent[1]),int(vent[2]),int(vent[3])]
  vents.append(vent)
  
mapCoords = list(map(lambda s: [max(s[0],s[2]),max(s[1],s[3])], vents))


def maxCoords(a, b):
  return [max(a[0],b[0]),max(a[1],b[1])]

corner  = reduce(maxCoords, mapCoords)

ocean = [[0 for x in range(corner[1] + 1)] for y in range(corner[0] + 1)]

for coords in vents:
  if (coords[0] == coords[2]):
    for y in range(min(coords[1],coords[3]), max(coords[1],coords[3]) + 1):
      ocean[int(coords[0])][y] += 1
  elif (coords[1] == coords[3]):
    for x in range(min(coords[0],coords[2]),max(coords[0],coords[2]) + 1):
      ocean[x][int(coords[1])] += 1
  else:
    length = max(coords[0],coords[2]) - min(coords[0],coords[2]) + 1
    plusX = coords[2] > coords[0]
    plusY = coords[3] > coords[1]
    x = coords[0]
    y = coords[1]
    for i in range(0, length):
      x = coords[0] + i if plusX else coords[0] - i
      y = coords[1] + i if plusY else coords[1] - i
      ocean[x][y] += 1

 
answer = reduce(lambda x, y: x + sum(map(lambda z: z > 1, y)), ocean, 0)
print(answer)

  
