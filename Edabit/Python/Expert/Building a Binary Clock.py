# https://edabit.com/challenge/E9Wkppxyo763XywBe
# 08.08.2024
# Expect

def modification_str(txt, i, new_value):
    txt = list(txt)
    txt[i] = new_value
    txt = ''.join(txt)
    return txt

def binary_clock(time):
    result = [' n n n', ' nnnnn'] +  ['nnnnnn'] * 2
    time = time.split(':')
    conv_bin = lambda x: str(bin(x))[2:].zfill(4)
    for i in range(len(time)):
        time[i] = list(time[i])
        time[i] = list(map(int, time[i]))
        time[i] = list(map(conv_bin, time[i]))
    for i in range(4):
        for j in range(6):
            if result[i][j] == 'n':
                result[i] = modification_str(result[i], j, time[j//2][j%2][i])
    return result

def binary_clock2(time):
    pattern = [' n n n', ' nnnnn'] + ['nnnnnn'] * 2
    result = [''] * 4
    time = time.split(':')
    conv_bin = lambda x: str(bin(x))[2:].zfill(4)
    for i in range(len(time)):
        time[i] = list(time[i])
        time[i] = list(map(int, time[i]))
        time[i] = list(map(conv_bin, time[i]))
    for i in range(4):
        for j in range(6):
            if pattern[i][j] == 'n':
                result[i] += time[j//2][j%2][i]
            else:
                result[i] += ' '
    return result

