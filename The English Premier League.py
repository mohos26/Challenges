# https://edabit.com/challenge/ajpDcExmmPy4Qaezi
# 08.03.2023
# Very Hard


def EPLResult(Table, team):
    len_table = len(Table)
    for i in range(len_table):
        Table[i].append(Table[i][2] * 3 + Table[i][3])
    Table.sort(reverse=True, key=lambda x: x[-1])

    lst, d = [], 1
    while True:
        for i in range(d, len_table):
            if Table[i][6] == Table[i - 1][6]:
                lst.append([i-1, []])
                for j in range(i - 1, len_table):
                    if Table[j][6] == Table[i - 1][6]:
                        lst[-1][1].append(Table[j])
                    else:
                        d = j
                        break
                break
        else:
            break
    for i in range(len(lst)):
        lst[i][1].sort(reverse=True, key=lambda x: x[5])

    for i in lst:
        for j in range(len(i[1])):
            Table.pop(i[0]+j)
            Table.insert(i[0]+j, i[1][j])

    for i in range(len_table):
        if Table[i][0] == team:
            if i < 3:
                ar = ["st", "nd", "rd"][i]
                return f'{Table[i][0]} came {i+1}{ar} with {Table[i][6]} points and a goal difference of {Table[i][5]}!'
            return f'{Table[i][0]} came {i+1}th with {Table[i][6]} points and a goal difference of {Table[i][5]}!'


table = [
    ['Arsenal', 38, 14, 14, 10, 8],
    ['Aston Villa', 38, 9, 8, 21, -26],
    ['Bournemouth', 38, 9, 7, 22, -26],
    ['Brighton', 38, 9, 14, 15, -15],
    ['Burnley', 38, 15, 9, 14, -7],
    ['Chelsea', 38, 20, 6, 12, 15],
    ['Crystal Palace', 38, 11, 10, 17, -19],
    ['Everton', 38, 13, 10, 15, -12],
    ['Leicester City', 38, 18, 8, 12, 26],
    ['Liverpool', 38, 32, 3, 3, 52],
    ['Manchester City', 38, 26, 3, 9, 67],
    ['Manchester Utd', 38, 18, 12, 8, 30],
    ['Newcastle', 38, 11, 11, 16, -20],
    ['Norwich', 38, 5, 6, 27, -49],
    ['Sheffield Utd', 38, 14, 12, 12, 0],
    ['Southampton', 38, 15, 7, 16, -9],
    ['Tottenham', 38, 16, 11, 11, 14],
    ['Watford', 38, 8, 10, 20, -28],
    ['West Ham', 38, 10, 9, 19, -13],
    ['Wolves', 38, 15, 14, 9, 11]
]
