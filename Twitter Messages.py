# https://edabit.com/challenge/8WvpPQto44PqNLSqJ
# 08.07.2023
# Hard


def pad(message):
    if len(message) < 140:
        if len(message) % 2 == 0:
            message += ' '
        message += 'lo'*((139-len(message))//2) + 'l'
    return message
