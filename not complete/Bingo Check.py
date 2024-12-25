# https://edabit.com/challenge/mJpjpgxkxvTY4Qbwf
# Very Hard


def list_count(lst, iteam):
    count = 0
    for arg in lst:
        if arg == iteam:
            count += 1
    return count

def bingo_check(board):
    txt = map(lambda x: str(x), board[0] + board[1] + board[2] + board[3] + board[4])
    length = list_count(txt, 'x')
    if length >= 5:
        lst = []
        i = 0
        for _ in range(length):
            i += txt[i:].index('x')
            lst.append([i//5, i%5])
            i += 1
        lst2 = map(lambda l: l[0], lst)
        lst3 = map(lambda l: l[1], lst)
        if max(map(lambda x: list_count(lst2, x), list(set(lst2)))) == 5 or \
                max(map(lambda x: list_count(lst3, x), list(set(lst3)))) == 5:
            return True

    return False

print(bingo_check([
  [45, "x", 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, 39, 44],
  [21, "x", 24, 30, 52]
]))
