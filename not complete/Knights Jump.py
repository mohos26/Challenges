# https://edabit.com/challenge/mm2fm6ynbR7HQQm9z
# 22.03.2023
# Expect

def knights_jump(place):
    letters = 'ABCDEFGH'
    lip = letters.index(place[0])
    ip = int(place[1])
    places = [
        [lip + 1, ip + 2],
        [lip - 1, ip + 2],
        [lip + 1, ip - 2],
        [lip - 1, ip - 2],
        [lip + 2, ip + 1],
        [lip + 2, ip - 1],
        [lip - 2, ip + 1],
        [lip - 2, ip - 1]
    ]
    result = ''
    for letter, number in places:
        if -1 < letter < 8 and 0 < number < 9:
            result += f'{letters[letter]}{number}, '
    return result.rstrip(', ')

def knights_jump_gpt(square):
    row = int(square[1])
    col = ord(square[0]) - ord('A') + 1
    moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]
    result = []
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if 1 <= new_row <= 8 and 1 <= new_col <= 8:
            result.append(chr(new_col + ord('A') - 1) + str(new_row))
    return ','.join(result)
