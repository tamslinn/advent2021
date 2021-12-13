f = open("day4.txt", "r")

numbers = f.readline().split(",")

def set_bit(value, bit):
    return value | (1<<bit)

boardmask = [0b00000,0b00000,0b00000,0b00000,0b00000]

boards = []
rowmasks = []
colmasks = []
board = []

winningboards = []
winningnum = 0

for num, line in enumerate(f, start=0):
  
  if num > 0:
    if line.strip() == '':
      if num > 1:
        boards.append(board.copy())
        rowmasks.append(boardmask.copy())
        colmasks.append(boardmask.copy())
      board = []
    else:
      board.append(line.strip().split())


for i, val in enumerate(numbers, start=0):
  for j, b in enumerate(boards):
    for y, line in enumerate(b):
      for pos, num in enumerate(line):
        if num == val:
          line[pos] = 'x'
          rowmasks[j][y] = set_bit(rowmasks[j][y],pos)
          colmasks[j][pos] = set_bit(colmasks[j][pos],y)
         
  if (i > 4):
    found = False
    
    for p, mask in enumerate(rowmasks):
      if (31 in mask):
        #print(p)
        found = True
        if p not in winningboards:
           winningboards.append(p)
        #break
    for q, mask in enumerate(colmasks):
      if (31 in mask):
        #print(q)
        found = True
        if q not in winningboards:
          winningboards.append(q)
        #break
    print(winningboards)
    if len(winningboards) == len(boards):
      winningnum = int(val)
      break

    

print('Winning board ' + str(winningboards[len(winningboards)-1]))   
print('Winning num' + str(winningnum))
board = boards[winningboards[len(winningboards)-1]]
print(board)
result = 0
for row in board:
  for val in row:
    if val != 'x':
      result = result + int(val)
result = result * winningnum
print(result)