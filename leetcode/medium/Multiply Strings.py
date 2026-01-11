# https://leetcode.com/problems/multiply-strings
# 26.12.2026


class Solution:
    def ft_aid(self, a, b):
        last = 0
        res = ''
        for i in b[::-1]:
            res = str((a * int(i) + last) % 10) + res
            last = (a * int(i) + last) // 10
        res = str(last) + res if last else res
        return res

    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i, n in enumerate(num2[::-1]):
            res += int(self.ft_aid(int(n), num1))* 10**i
        return str(res)

