# https://edabit.com/challenge/iLLqX4nC2HT2xxg3F
# Very Hard

def deepest(lst, aid=1, v_max=1):
    if not len(lst):
        return v_max
    elif type(lst[0]) == list:
        return deepest(lst[0], aid=aid+1, v_max=v_max) + deepest(lst[1:], v_max=v_max)
    return deepest(lst[1:], aid=aid, v_max=max(v_max, aid))
