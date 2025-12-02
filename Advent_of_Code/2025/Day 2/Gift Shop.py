def twice(s):
    return int(s[:len(s)//2] * 2)

with open("/tmp/input.txt") as file:
    ranges = [r.split('-') for r in file.read().split(',')]
    res = 0
    for a, b in ranges:
        for n in range(int(a), int(b) + 1):
            s = str(n)
            if not len(s) % 2 and n == twice(s):
                res += n
                print(n)
    print(res)

