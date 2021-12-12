f = open("day9.txt", "r")
heights = []

for x in f:
    heights.append(list(map(int, list(x.strip()))))

lows = 0
sum = 0

for row, vals in enumerate(heights):
    for col, val in enumerate(vals):
        low = True
        if val == 9:
            low = False
        else:
            if col > 0 and heights[row][col - 1] < val:
                low = False
            if col < len(vals) - 1 and heights[row][col + 1] < val:
                low = False
            if row  > 0  and heights[row - 1][col] < val:
                low = False
            if row < len(heights) - 1 and heights[row + 1][col] < val:

                low = False
        if low:
            sum += 1 + val
            lows += 1
            print("low " + str(row) + "," + str(col))

print(lows)
print(sum)