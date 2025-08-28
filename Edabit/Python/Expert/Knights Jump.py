# https://edabit.com/challenge/mm2fm6ynbR7HQQm9z
# 22.03.2023
# Expect

def knights_jump(place):
    letters = 'ABCDEFGH'
    lip = letters.index(place[0])
    ip = int(place[1])
    places = [
        [lip - 1, ip - 2],
        [lip + 1, ip - 2],
        [lip - 2, ip - 1],
        [lip + 2, ip - 1],
        [lip - 2, ip + 1],
        [lip + 2, ip + 1],
        [lip - 1, ip + 2],
        [lip + 1, ip + 2]
    ]
    result = []
    for letter, number in places:
        if -1 < letter < 8 and 0 < number < 9:
            result.append(f'{letters[letter]}{number}')
    return ','.join(result)
