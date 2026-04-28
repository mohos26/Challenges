# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 24.09.2025


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left = prices[0]
        for right in prices[1:]:
            res = max(res, right - left)
            if right < left:
                left = right
        return res


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        _max = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            res = max(_max - prices[i], res)
            _max = max(_max, prices[i])
        return res

