f = open("day6.txt", "r")
fish = f.readline().split(',')
fish = list(map(int, fish))

for day in range(0,80):
  for i in range(0,len(fish)):
    if fish[i] == 0:
      fish[i] = 6
      fish.append(8)
    else:
      fish[i] = fish[i] - 1



print(len(fish))