# https://edabit.com/challenge/hAsdEPWwufWoJos32
# Meduim
# 18.08.2024

def no_yelling(phrase):
    if len(phrase) == 1:
        return phrase
    elif phrase == len(phrase)*'!' or phrase == len(phrase)*'?':
        return phrase[0]
    return phrase[0] + no_yelling(phrase[1:])

