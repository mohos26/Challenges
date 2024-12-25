# https://edabit.com/challenge/biJPWHr486Y4cPLnD
# 09.06.24
# Hard


def chunkify(lst, size):
    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i+size])
    return result
