import statistics

f = open("day8.txt", "r")

total = 0

for x in f:
    
    numbers = ['' for x in range(0,10)]
    parts = x.split('|')
    input = parts[0].split()
    
    numbers[1] = sorted(list(filter(lambda x: len(x) == 2, input))[0])
    numbers[4] = sorted(list(filter(lambda x: len(x) == 4, input))[0])
    numbers[7] = sorted(list(filter(lambda x: len(x) == 3, input))[0])
    numbers[8] = sorted(list(filter(lambda x: len(x) == 7, input))[0])

    # list 1 contains all of list 2 
    # all(elem in list1  for elem in list2)

    sixes = list(filter(lambda x: len(x) == 6, input))
    numbers[6] = sorted(list(filter(lambda x: not all(elem in sorted(x)  for elem in numbers[1]), sixes))[0])
    numbers[9] = sorted(list(filter(lambda x: all(elem in sorted(x)  for elem in numbers[4]), sixes))[0])
    numbers[0] = sorted(list(filter(lambda x: sorted(x) != numbers[6] and sorted(x) != numbers[9], sixes))[0])

    fives = list(filter(lambda x: len(x) == 5, input))

    numbers[5] = sorted(list(filter(lambda x: all(elem in numbers[6]  for elem in sorted(x)), fives))[0])    
    numbers[3] = sorted(list(filter(lambda x: all(elem in sorted(x)  for elem in numbers[1]), fives))[0])    
    numbers[2] = sorted(list(filter(lambda x: sorted(x) != numbers[5] and sorted(x) != numbers[3], fives))[0])

    output = parts[1].split() 
    
    result = ""
    for val in output:
        result += str(numbers.index(sorted(val)))
        
    total += int(result)

print(total)    
    
    

