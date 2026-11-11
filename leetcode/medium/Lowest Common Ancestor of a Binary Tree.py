# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 11.11.2026


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def dfs(node):
            if not node:
                return 0b00
            curr = ((p == node) << 1) | (q == node)
            curr |= dfs(node.left) | dfs(node.right)
            if curr == 0b11:
                nonlocal res
                if not res:
                    res = node
            return curr
        dfs(root)
        return res

