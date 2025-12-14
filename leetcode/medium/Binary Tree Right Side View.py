# https://leetcode.com/problems/binary-tree-right-side-view/
# 14.12.2025

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [None] * self.maxDepth(root)
        def dfs(node, depth):
            if not node:
                return
            nonlocal res
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            res[depth] = node.val
        dfs(root, 0)
        return res

