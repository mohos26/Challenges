# https://edabit.com/challenge/G5FXsvc8hD6DqnCKx
# 09.06.2023
# Hard


def convert_time(time):
    Time = time.split()
    if len(Time) == 2:
        Time.append(2)
    else:
        Time.append(1)

    var = Time[0].split(':')
    Time = [int(var[0]), var[1]] + Time[1:]
    if Time[2] == 1:
        if Time[0] > 12:
            Time[0] -= 12
            Time.append('pm')
        else:
            Time.append('am')
        Time[0] = str(Time[0])
        return ':'.join(Time[:2]) + ' ' + Time[3]
    else:
        Time.pop(-1)
        if Time[2] == 'pm':
            Time[0] += 12
        elif Time[0] == 12:
            Time[0] = 0
        Time.pop(-1)
        Time[0] = str(Time[0])
        return ':'.join(Time)

