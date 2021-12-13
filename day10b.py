f = open("day10.txt", "r")

open = ['(','{','<','[']
pairs = { ')': '(', '}': '{','>': '<',']': '['}
points = { '(': 1, '[': 2, '{': 3,'<': 4}
scores = []

for x in f:
    corrupt = False
    brackets = []
    line = list(x.strip())
    for c in line:
        if c in open:
            brackets.append(c)
        else:
            close = brackets.pop()
            if close != pairs[c]:
                corrupt = True
    if not corrupt and len(brackets) > 0:
        lineScore = 0
        for i in range(0, len(brackets)):
            lineScore = lineScore * 5
            lineScore = lineScore + points[brackets.pop()]
        scores.append(lineScore)

scores.sort()
print(scores[int((len(scores) - 1)/2)])



