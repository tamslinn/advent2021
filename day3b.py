f = open("day3.txt", "r")
strings = f.read().splitlines()


def get_bit(value, bit_index):
  return (value >> bit_index) & 1

ints = list(map(lambda x: int(x, base=2), strings))

pos = 11
while len(ints) > 1:
    count = 0
    for x in ints:
        count += get_bit(x,pos)

    selected = 0
    if count >= len(ints)/2:
        selected = 1

    ints = list(filter(lambda x: get_bit(x,pos) == selected, ints))

    print(ints)
    pos -=1

ints2 = list(map(lambda x: int(x, base=2), strings))

pos = 11
while len(ints2) > 1:
    count = 0
    for x in ints2:
        count += get_bit(x,pos)

    selected = 0
    if count < len(ints2)/2:
        selected = 1

    ints2 = list(filter(lambda x: get_bit(x,pos) == selected, ints2))

    print(ints2)
    pos -=1

print(ints[0] * ints2[0])