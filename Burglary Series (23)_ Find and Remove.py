# https://edabit.com/challenge/WxkFoXTLYiAq57uDq
# Very Hard
# 21.08.2024


def find_and_remove(dct):
    lst = []
    for main_key in dct.keys():
        for key, value in dct[main_key].items():
            if value.isdigit():
                dct[main_key][key] = int(value)
            else:
                lst.append([main_key, key])
    for main_key, key in lst:
        dct[main_key].pop(key)
    return dct

