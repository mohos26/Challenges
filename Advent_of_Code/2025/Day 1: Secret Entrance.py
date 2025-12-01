from math import ceil


with open('input.txt') as file:
    start, result = 50, 0
    while (line := file.readline().strip()):
        sing = 1
        if line[0] == 'L':
            sing = -1
        num = int(line[1:]) * sing
        start += num
        if start < 0:
            start += (ceil(start / 100) * 100)
        start %= 100
        if not start:
            result += 1
    print(result)

