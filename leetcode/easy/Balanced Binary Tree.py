# https://leetcode.com/problems/balanced-binary-tree/
# 10.12.2026


class Solution: # Top-Down DFS o(n**2)
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

class Solution_2: # Bottom-Up DFS o(n)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            left_depth = dfs(node.left)
            if left_depth == -1:
                return -1
            right_depth = dfs(node.right)
            if right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1
            return 1 + max(left_depth, right_depth)
        return dfs(root) != -1

