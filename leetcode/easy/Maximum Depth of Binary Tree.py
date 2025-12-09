# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 08.12.2025


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

