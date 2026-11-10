# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# 10.11.2026


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        res = 0
        def dfs(node, direction):
            if not node:
                return 0
            nonlocal res
            left = dfs(node.left, 1) + 1
            right = dfs(node.right, 0) + 1
            res = max(res, left, right)
            return (right if direction else left)
        dfs(root, 0)
        return res - 1 if res > 0 else 0

