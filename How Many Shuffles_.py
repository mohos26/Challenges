# https://edabit.com/challenge/quMt6typruySiNSAJ
# Very Hard
# 05.04.2024


def shuffle_count(num):
    """    def suff(lst):
        l1, l2, result = lst[:len(lst) // 2], lst[len(lst) // 2:], []
        for i in range(len(lst) // 2):
            result.append(l1[i])
            result.append(l2[i])
        return result
    step = 1
    lst = list(range(1, num+1))
    result = suff(lst)
    while result != lst:
        step += 1
        result = suff(result)
    return step"""
    step, num_d2, lst = 0, num // 2, list(range(1, num+1))
    result = lst.copy()
    while True:
        step += 1
        l1, l2 = result[:num_d2], result[num_d2:]
        result.clear()
        for i in range(num_d2):
            result.append(l1[i])
            result.append(l2[i])
        if result == lst:
            break
    return step
