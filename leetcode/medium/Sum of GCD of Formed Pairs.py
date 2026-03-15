# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/
# 15.03.2026


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        lst = []
        _max = float("-inf")
        for n in nums:
            _max = max(n, _max)
            lst.append(gcd(n, _max))
        res = 0
        lst = deque(sorted(lst))
        while len(lst) > 1:
            a, b = lst.popleft(), lst.pop()
            res += gcd(a, b)
        return res

