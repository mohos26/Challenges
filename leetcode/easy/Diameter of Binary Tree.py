# https://leetcode.com/problems/diameter-of-binary-tree/
# 09.12.2025


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        diameter_left = self.diameterOfBinaryTree(root.left)
        diameter_right = self.diameterOfBinaryTree(root.right)
        return max(self.maxDepth(root.left) + self.maxDepth(root.right), diameter_left, diameter_right)

