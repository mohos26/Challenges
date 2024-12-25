# https://edabit.com/challenge/vLLXeQH5tgyvbzYZS
# very Hard
# 11.08.2024


from math import sqrt, floor

def ft_factor(n):
    result = []
    for i in range(2, n//2 + 1):
        if n % i == 0:
            result.append(i)
    return result

def is_prim_pyth_triple(lst):
    lst1 = ft_factor(lst[0]) + ft_factor(lst[1]) + ft_factor(lst[2])
    n_max = lst.index(max(lst))
    lst2 = lst[:n_max] + lst[n_max+1:]
    return len(lst1) == len(list(set(lst1))) and lst[n_max]**2 == (lst2[0]**2 + lst2[1]**2)

