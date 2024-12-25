# https://edabit.com/challenge/3Eia4oLLCcyyLN2L7
# 15.03.2023
# Medium


def remove_repeats(t):
    t1 = r = ''
    for i in t:
        if i != r:
            t1 += i
            r = i
    return t1

def remove_repeats_gpt(word):
    result = ""
    for i in range(len(word)):
        if i == 0 or word[i] != word[i-1]:
            result += word[i]
    return result
