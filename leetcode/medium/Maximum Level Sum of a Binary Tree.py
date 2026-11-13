# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# 13.11.2026


class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        i = 1
        d = deque([root])
        res = (float("-inf"), 0)
        while d:
            _sum = 0
            for _ in range(len(d)):
                curr = d.popleft()
                _sum += curr.val
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
            if _sum > res[0]:
                res = _sum, i
            i += 1
        return res[1]

