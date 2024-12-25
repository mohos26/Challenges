# https://edabit.com/challenge/Box2A6Rb94ao8wAye
# Meduim
# 07.08.2024

def leader(lst):
    result = []
    for i in range(len(lst)):
        for j in lst[i+1:]:
            if lst[i] < j:
                break
        else:
            result.append(lst[i])
    return result

def leader2(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] > max(lst[i+1:] + [min(lst)]):
            result.append(lst[i])
    return result

