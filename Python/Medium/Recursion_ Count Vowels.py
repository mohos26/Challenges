# https://edabit.com/challenge/nHxBoXmRYq5vnoEnq
# Meduim
# 09.08.2024


def vowels(txt):
    if not txt:
        return 0
    var = txt[0] in "aeiou"
    return var + vowels(txt[1:])

