
f = open("day10.txt", "r")

errors = []
open = ['(','{','<','[']
pairs = { ')': '(', '}': '{','>': '<',']': '['}
scores = { ')': 3, '}': 1197,'>': 25137,']': 57}

for x in f:
    brackets = []
    line = list(x.strip())
    for c in line:
        if c in open:
            brackets.append(c)
        else:
            close = brackets.pop()
            if close != pairs[c]:
                errors.append(c)
                break

score = 0

for key, value in scores.items():
    score += errors.count(key) * value

print(score)