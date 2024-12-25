# https://edabit.com/challenge/WWw5gG3c4RN8dr6QD
# Very Easy
# 11.09.2024


def after_n_months(year, month):
    if year == None:
        return 'year missing'
    if month == None:
        return 'month missing'
    return year + month//12

