# https://edabit.com/challenge/oiHH7qocTyM3JqNf8
# 18.08.2023
# Medium


def move(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for letter in word:
        result += letters[letters.index(letter)+1]
    return result
