# https://edabit.com/challenge/ENxiMBnKzf5HQgin2
# 23.08.2023
# Expect


def pascal_row(n):
    lst = [[1]]
    for i in range(1, n + 1):
        lst.append([1] + [0] * (i - 1) + [1])
        for j in range(1, i):
            lst[i][j] = lst[i - 1][j - 1] + lst[i - 1][j]
    return lst[n]

def pascal_row_remaster(n):
    """lst = [1]
    if n == 0:
        return lst
    for i in range(1, (n + 1) // 2):
        # ((1 + ((1 / i) * (n - (2 * i - 1)))) * (lst[-1] / n)) * n
        lst.append(lst[-1]*((n-i+1)/i))
    if n % 2 == 0:
        i = n // 2
        return lst + [lst[-1]*((n-i+1)/i)] + lst[::-1]
    return lst + lst[::-1]"""
    if n == 0:
        return [1]

    row = [1]
    for i in range(1, (n + 1) // 2):
        new_value = int(row[-1] * (n - i + 1) / i)
        row.append(new_value)

    if n % 2 == 0:
        middle_value = int(row[-1] * ((n - (n // 2) - 1) / (n // 2)))
        return row + [middle_value] + row[::-1]

    return row + row[::-1]

def pascal_row_gpt(n):
    if n == 0:
        return [1]

    row = [1]
    prev_value = 1

    for k in range(1, n + 1):
        curr_value = (prev_value * (n - k + 1)) // k
        row.append(curr_value)
        prev_value = curr_value

    return row
