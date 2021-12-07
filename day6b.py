f = open("day6.txt", "r")
fish = f.readline().split(',')

days = 256

fishByAge = [0,fish.count('1'),fish.count('2'),fish.count('3'),fish.count('4'),fish.count('5'),0,0,0]

for day in range(0,days):
  newFishByAge = [0 for x in range(0,9)]
  for i in range(0,len(fishByAge)):
      if i == 0:
          newFishByAge[6] = fishByAge[0]
          newFishByAge[8] = fishByAge[0]
      else:
          newFishByAge[i-1] = newFishByAge[i-1] + fishByAge[i]
  
  fishByAge = newFishByAge 

print(sum(fishByAge))