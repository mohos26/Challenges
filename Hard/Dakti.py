# https://edabit.com/challenge/EJRa8efMPoCwzLNRW
# 28.05.2024
# Very Hard
import re


def dakiti(sentence):
    var = sentence.split()
    result = ['']*len(var)
    for i in var:
        for j in range(len(i)):
            if i[j].isdigit():
                result[int(i[j])-1] = i[:j] + i[j+1:]
                break
    return ' '.join(result)
