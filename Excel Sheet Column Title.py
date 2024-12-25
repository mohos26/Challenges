# https://edabit.com/challenge/7mp5P99QqnQHePe3P
# Expert

from string import ascii_uppercase as letters
from math import log


def convert_to_title(n):
    result = ''
    length = int(log(25*(n+1), 26))
    for i in range(length, 0, -1):
        var = (25*n-26**i+1)//(25*26**(i-1))+1
        result += letters[var-1]
        n -= 26**(i-1)*var
    return result


# ---------------------------------------------------

def add(s):
    if s == len(s)*letters[-1]:
        return (len(s)+1)*letters[0]
    result = ''
    var = 1
    for i in s[::-1]:
        if i == letters[-1] and var:
            result += letters[0]
        elif var:
            result += letters[letters.index(i) + 1]
            var = 0
        else:
            result += i
    return result[::-1]


def convert_to_title_2(n):
    # Time out
    result = letters[0]
    for i in range(n):
        result = add(result)
    return result
