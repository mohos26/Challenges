# https://edabit.com/challenge/sibD9TFg7pmQuzJxW
# Very Hard
# 15.08.2024


def ist(n):
    if n < 10:
        return [0, n]
    return [n//10, n%10]

def stem_plot(lst):
    result = []
    lst2 = []
    for i in lst:
        var = ist(i)
        if var[0] in lst2:
            result[lst2.index(var[0])].append(var[1])
        else:
            lst2.append(var[0])
            result.append(var)
    result.sort()
    for i in range(len(result)):
        var = list(map(str, [result[i][0]] + sorted(result[i][1:])))
        var2 = ' '.join([' | '.join(var[:2])] + var[2:])
        result[i] = var2
    return result

