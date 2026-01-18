# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# 18.01.2026


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, n):
            if node is None:
                return
            n = n * 10 + node.val
            if node.left == node.right:
                nonlocal res
                res += n
            else:
                dfs(node.left, n)
                dfs(node.right, n)
        dfs(root, 0)
        return res

