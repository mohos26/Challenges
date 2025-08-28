# https://edabit.com/challenge/BP4nrcAhaZzKeDq5y
# 10.07.2025
# Very Hard


def find_anagrams(s, p):
    lst, remaining_chars, i, start_index = [], list(p), 0, 0
    while i < len(s):
        if not remaining_chars:
            remaining_chars = list(p)
            lst.append(start_index)
            i -= len(p) - 1
        if s[i] in remaining_chars:
            if len(remaining_chars) == len(p):
                start_index = i
            remaining_chars.remove(s[i])
        elif len(remaining_chars) != len(p):
            i -= len(p) - len(remaining_chars)
            remaining_chars = list(p)
        i += 1
    if not remaining_chars:
        lst.append(start_index)
    return lst
