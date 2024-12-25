# https://edabit.com/challenge/iG5vcwd282T4t7h6r
# Medium
# 20.11.2023


def str_to_dict(lst):
    result = dict()
    for i in lst:
        var = i.split('=')
        result.update({var[0]: var[1]})
    return result


def str_to_dict_gpt(str_list):
    result_dict = {}
    for item in str_list:
        key, value = item.split('=')
        result_dict[key] = value
    return result_dict
