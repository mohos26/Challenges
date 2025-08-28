# https://edabit.com/challenge/3vhXY6fdDhYpfE4vF
# Expect


def clockwise_decipher(msg):
    result = ''
    for i in range(0, len(msg), 4):
        result += msg[i+4:i-1:-1]
    return result
