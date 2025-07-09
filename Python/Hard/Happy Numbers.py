# https://edabit.com/challenge/knWLLoi87YbCmKJS4
# 09.07.2025
# Hard

def happy(n):
    count = 0
    while True:
        aid = 0
        for i in str(n):
            aid += int(i)**2
        if aid == 1:
            break
        if count > 100:
            return False
        count += 1
        n = aid
    return True
