# https://leetcode.com/problems/invert-binary-tree
# 08.12.2025


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        return TreeNode(root.val, left, right)

