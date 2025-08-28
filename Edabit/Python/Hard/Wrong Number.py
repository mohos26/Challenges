# https://edabit.com/challenge/7cJ8q3gRoYEj2A3jn
# 2.03.2024
# Very Hard


def wrong_number(lst):
    for arg in lst:
        if sum(arg[:-1]) != arg[-1]:
            for j in range(4):
                if lst[0][j] + lst[1][j] + lst[2][j] != lst[3][j]:
                    return (arg[3] - sum(arg[1:3]), arg[3] - sum(arg[:3]), arg[3] - sum(arg[:2]), sum(arg[:3]))[j]

# ChatGPT could not find a correct solution
