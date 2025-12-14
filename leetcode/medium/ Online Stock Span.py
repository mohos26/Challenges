# https://leetcode.com/problems/online-stock-span/
# 14.12.2025


class StockSpanner:
    def __init__(self):
        self.stack = deque()

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, res))
        return res

