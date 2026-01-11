# https://leetcode.com/problems/count-good-meals
# 29.11.2026


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        result = 0
        d = Counter(deliciousness)
        for n in d:
            for i in range(floor(log2(max(1, n))), 22):
                if 2**i - n in d:
                    if 2**i - n == n:
                        if d[n] > 1:
                            result += d[n] * (d[n] - 1) // 2
                    else:
                        result += d[n] * d[2**i-n]
            d[n] = 0
        return result % (10**9+7)


