# https://edabit.com/challenge/5D3iXJSkSreRzNS8W
# Very Hard
# 07.09.2024


def news_at_ten(txt, n):
    result = []
    txt = n*' ' + txt + n*' '
    for i in range(0, len(txt)-n+1):
        result.append(txt[i:n+i])
    return result

