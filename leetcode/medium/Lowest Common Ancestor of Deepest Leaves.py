# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# 18.01.2026


class Solution:
    def maxDeepest(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDeepest(root.left), self.maxDeepest(root.right))

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        _max = self.maxDeepest(root)
        res = None
        def dfs(node, deep):
            if not node:
                return deep
            deepest_left = dfs(node.left, deep + 1)
            deepest_right = dfs(node.right, deep + 1)
            if deepest_left == deepest_right and deepest_left == _max:
                nonlocal res
                res = node
            return max(deepest_left, deepest_right)
        dfs(root, 0)
        return res

