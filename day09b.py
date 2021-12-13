f = open("day9.txt", "r")
heights = []

for x in f:
    heights.append(list(x.strip()))

basin = 0

def joinBasins(oldTag, newTag):
    for row, vals in enumerate(heights):
        for col, val in enumerate(vals):
            if heights[row][col] == oldTag:
                heights[row][col] = newTag

for row, vals in enumerate(heights):
    basin += 1
    for col, val in enumerate(vals):
        if val == '9':
            basin += 1
        else:
            basinTag = 'B' + str(basin)
            heights[row][col] = basinTag
            if row  > 0 and heights[row - 1][col] != '9' and heights[row - 1][col] != basinTag:
                joinBasins(heights[row - 1][col], basinTag)
              

sizes = []
for i in range(1,basin + 1):
    count = 0
    basinTag = 'B' + str(i)
    for row in heights:
        count += row.count(basinTag)   
    if (count > 0):
        sizes.append(count)

sizes.sort(reverse=True)
print(sizes[0] * sizes[1] * sizes[2])