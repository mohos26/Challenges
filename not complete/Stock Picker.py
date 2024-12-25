# https://edabit.com/challenge/DqLngKnnJcZyPMctn
# 19.07.2023
# Hard


def stock_picker(lst):
    lst2 = []
    for i, arg in enumerate(lst[:-1]):
        for j in lst[i+1:]:
            lst2.append(j - arg)
    return sorted(lst2)[-1]

def stock_picker_gpt(prices):
    max_profit = -1
    buy_day, sell_day = None, None
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
                buy_day = i
                sell_day = j
    if max_profit == -1:
        return -1
    return max_profit
