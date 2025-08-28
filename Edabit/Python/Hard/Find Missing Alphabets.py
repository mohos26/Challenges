# https://edabit.com/challenge/SQZoHFDfizBTP4HSx
# very Hard
#18.08.2024


def missing_alphabets(txt):
    lst = []
    for i in set(list(txt)):
        lst.append(txt.count(i))
    result = list('abcdefghijklmnopqrstuvwxyz'*max(lst))
    for i in txt:
        result.remove(i)
    return ''.join(sorted(result))

