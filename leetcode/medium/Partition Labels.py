# https://leetcode.com/problems/partition-labels/description/
# 29.05.2026


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, letter in enumerate(s):
            d[letter] = i
        res = []
        right = last = -1
        for i, letter in enumerate(s):
            right = max(right, d[letter])
            if right == i:
                res.append(right - last)
                last = right
        return res
