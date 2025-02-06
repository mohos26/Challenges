# https://edabit.com/challenge/tgd8bCn8QtrqL4sdy
# 28.10.2024
# Very Hard


def minesweeper(grid):
    aid, lst, i = ''.join(grid[0] + grid[1] + grid[2]), [], 0
    for _ in range(aid.count('?')):
        i += aid[i:].index('?')
        a, b, Sum = i//3, i%3, 0
        for x, y in [a-1, b-1], [a-1, b], [a-1, b+1], [a, b-1], [a, b+1], [a+1, b-1], [a+1, b], [a+1, b+1]:
            if 0 <= x <= 2 and 0 <= y <= 2 and grid[x][y] == '#':
                Sum += 1
        grid[a][b] = str(Sum)
        i += 1
    return grid

