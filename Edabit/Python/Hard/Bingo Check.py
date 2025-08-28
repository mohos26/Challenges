# https://edabit.com/challenge/mJpjpgxkxvTY4Qbwf
# Very Hard


def check_afo9i(lst):
    for i in lst:
        if i > 4:
            break
        for j in range(1, 5):
            if i + j*5 not in lst:
                break
        else:
            return True
    return False

def check_3amodi(lst):
    for i in range(len(lst)):
        if not lst[i]%5  and list(range(lst[i], lst[i]+5)) == lst[i:i+5]:
            return True
    return False

def check_mail(lst):
    if 0 in lst:
        loop = range(1, 5)
    elif 4 in lst:
        loop = range(4, 0)
    else:
        return False
    aid = 5
    for i in loop:
        if aid + i not in lst:
            break
        aid += 5
    else:
        return True
    return False

def bingo_check(board):
    lst = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'x':
                lst.append(i*5 + j)
    if check_afo9i(lst) or check_3amodi(lst) or check_mail(lst):
        return True
    return False
