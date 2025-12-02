def repeated(s):
    return s in (s + s)[1: -1]

with open("/tmp/input.txt") as file:
    ranges = [r.split('-') for r in file.read().split(',')]
    res = 0
    for a, b in ranges:
        for n in range(int(a), int(b) + 1):
            if repeated(str(n)):
                res += n
    print(res)

