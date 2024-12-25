# https://edabit.com/challenge/uhLCMpDLcyozWqSRP
# Expert


def find_path(tickets):
    Len = len(tickets)
    lst = []
    result = ['A']
    while tickets:
        lst = []
        for i in range(len(tickets)):
            if tickets[i][0] == result[-1]:
                lst.append(tickets[i])
        var = sorted(lst)[0]
        result += var[1]
        tickets.remove(var)
    return result
