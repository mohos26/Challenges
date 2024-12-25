# https://edabit.com/challenge/dix2XgYpxcsmaukA7
# 04.08.2024
# Very Hard

def Commonalities(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return i
    return n

def express_factors(n):
    lst = []
    result = []
    while n > 1:
        var = Commonalities(n)
        lst.append(str(var))
        n //= var
    lst2 = map(str, sorted(map(int, list(set(lst))), reverse=False))
    for i in lst2:
        result.append(i)
        var = lst.count(i)
        if var > 1:
            result[-1] += "^" + str(var)
        result.append("x")
    result.pop(-1)
    result = " ".join(result)
    return result
