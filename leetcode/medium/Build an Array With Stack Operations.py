# https://leetcode.com/problems/build-an-array-with-stack-operations
# 19.12.2026


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        res = []
        for n in range(1, n+1):
            if i == len(target):
                break
            res.append('Push')
            if n != target[i]:
                res.append('Pop')
            else:
                i += 1
        return res

