# https://edabit.com/challenge/Emdzxs23PRzSDuvk3
# 27.10.2024
# Hard


def pizza_points(customers, min_orders, min_price):
    res = []
    for customer, lst in customers.items():
        lst2 = []
        for iteam in lst:
            if iteam >= min_price:
                lst2.append(iteam)
        if len(lst2) >= min_orders:
            res.append([customer, len(lst2)])
    return list(map(lambda x: x[0], sorted(res, key=lambda x: x[1])))[::-1]

