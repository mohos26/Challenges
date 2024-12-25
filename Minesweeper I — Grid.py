# https://edabit.com/challenge/YDgtdP69Mn9pC73xN
# 29.05.24
# Very Hard


def num_grid(lst):
    result = []
    for i, row in enumerate(lst):
        result.append([])
        for j, arg in enumerate(row):
            if arg == '#':
                result[-1].append('#')
            else:
                result[-1].append(0)
                for d in [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]:
                    if 0 <= d[0] < len(lst) and 0 <= d[1] < len(lst[0]) and lst[d[0]][d[1]] == '#':
                        result[-1][-1] += 1
                result[-1][-1] = str(result[-1][-1])
    return result
