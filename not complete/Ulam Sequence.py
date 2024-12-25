# https://edabit.com/challenge/PPz4PqTJ5mXXa4MrW
# 01.04.2023
# Expect

"""Ulam implementation: 11.384456157684326 seconds
Ulam_gpt implementation: 0.48719120025634766 seconds"""


def ulam(n):
    ulam = [1, 2]
    for i in range(n - 2):
        lst, l = [], []
        for j in ulam:
            for d in ulam:
                if j != d and not ulam.count(j + d) and not lst.count([d, j, j + d]):
                    lst.append([j, d, j + d])
                    l.append(d+j)

        l.sort()
        while True:
            if l.count(l[0]) > 1:
                arg = l[0]
                for d in range(l.count(l[0])):
                    l.remove(arg)
            else:
                ulam.append(l[0])
                break

    return len(ulam)

def ulam_gpt(n):
    sequence = [1, 2]
    sums = {}
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            s = sequence[i] + sequence[j]
            if s not in sums:
                sums[s] = 1
            else:
                sums[s] += 1
    while len(sequence) < n:
        m = float('inf')
        for s in sums:
            if sums[s] == 1 and s > sequence[-1]:
                m = min(m, s)
        sequence.append(m)
        for i in range(len(sequence) - 1):
            s = sequence[i] + sequence[-1]
            if s not in sums:
                sums[s] = 1
            else:
                sums[s] += 1
    return sequence[n - 1]

