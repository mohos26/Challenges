# https://edabit.com/challenge/jT7PY2yTWTuxcqpJe
# 6.05.2023
# Expect


def spiral_order(matrix):
    lst = []
    for i in range(len(matrix)-1):
        lst += matrix[0]
        matrix.pop(0)
        for j in range(len(matrix)-1):
            lst.append(matrix[j][-1])
            matrix[j].pop(-1)
        if matrix:
            lst += matrix[-1][::-1]
            matrix.pop(-1)
    return lst
