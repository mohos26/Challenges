# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# 17.12.2025


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    res.append(prices[i] - prices[j])
                    break
            else:
                res.append(prices[i])
        return res

class Solutioni_2:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices.copy()
        stack = []
        for i, n in enumerate(prices):
            while stack and prices[stack[-1]] >= n:
                res[stack[-1]] -= n
                stack.pop()
            stack.append(i)
        return res

