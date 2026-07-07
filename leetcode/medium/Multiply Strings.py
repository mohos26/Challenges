# https://leetcode.com/problems/multiply-strings
# 26.12.2025


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


# 07.07.2026
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        lst = []
        num1, num2 = num1[::-1], num2[::-1]
        for i, n1 in enumerate(num1):
            rest = 0
            curr = ""
            for n2 in num2:
                rest += int(n1) * int(n2)
                curr = str(rest % 10) + curr
                rest //= 10
            if rest:
                curr = str(rest) + curr
            curr += '0' * i
            lst.append(curr)
        res = lst[0]
        for num in lst[1:]:
            tmp, res = res, ""
            _max = max(map(len, (num, tmp)))
            num, tmp = num.zfill(_max), tmp.zfill(_max)
            rest = 0
            for n1, n2 in zip(num[::-1], tmp[::-1]):
                rest += int(n1) + int(n2)
                res = str(rest % 10) + res
                rest //= 10
            if rest:
                res = str(rest) + res
        res = res.lstrip('0')
        return res if res else '0'

