# https://leetcode.com/problems/balanced-binary-tree/
# 10.12.2025


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root and abs(self.maxDepth(root.right) - self.maxDepth(root.left)) > 1:
            return False
        if root and (not self.isBalanced(root.left) or not self.isBalanced(root.right)):
            return False
        return True

