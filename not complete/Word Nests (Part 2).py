# https://edabit.com/challenge/ZwmfET5azpvBTWoQT
# 28.06.2023
# Very Hard


def valid_word_nest(word, nest):
    while True:
        nest = nest.split(word)
        if len(nest) == 1:
            return False
        elif nest == ['', '']:
            return True
        nest = ''.join(nest)


def valid_word_nest_gpt(word, nest):
    while len(nest) > len(word):
        start_index = nest.find(word)
        if start_index == -1:
            return False
        nest = nest[:start_index] + nest[start_index+len(word):]
    return nest == word
