# https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/
# 06.06.2026


class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        flag = False
        last = -1
        for i, b in enumerate(bin(n)[2:]):
            aid = i - last
            if b == '1' and aid > 1:
                if not flag:
                    flag = True
                else:
                    return False
            if b == '0':
                last = i
        return flag

