# https://edabit.com/challenge/dZhxErwMfyWymXbPN
# 26.10.2024
# Hard


def hangman(phrase, lst):
    for letter in phrase:
        if letter.isalpha() and letter.lower() not in lst: 
            phrase = phrase.replace(letter, '-')
    return phrase

print(hangman("helicopter", ["o", "e", "s"]))
