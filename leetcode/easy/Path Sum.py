# https://leetcode.com/problems/path-sum
# 26.12.2026


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        res = False
        def dfs(node, _sum):
            if not node:
                return
            if node.left is node.right and _sum + node.val == targetSum:
                nonlocal res
                res = True
                return
            dfs(node.left, _sum + node.val)
            dfs(node.right, _sum + node.val)
        dfs(root, 0)
        return res


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.left is root.right:
            return True if targetSum == root.val else False
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

