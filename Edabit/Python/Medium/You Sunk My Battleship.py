# https://edabit.com/challenge/cGqjxKhNqZPZ76zac
# 26.03.2023
# Medium



def fire(matrix, coordinates):
    if matrix['ABCDE'.index(coordinates[0])][int(coordinates[1]) - 1] == '.':
        return 'splash'
    return 'BOOM'
