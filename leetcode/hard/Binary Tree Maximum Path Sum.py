# https://leetcode.com/problems/binary-tree-maximum-path-sum
# 23.12.2026


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(node):
            if not node:
                return None
            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)

            if left is None and right is None:
                res = max(res, node.val)
                return node.val

            if left is None:
                res = max(res, right + node.val, node.val)
                return max(right + node.val, node.val)

            if right is None:
                res = max(res, left + node.val, node.val)
                return max(left + node.val, node.val)

            res = max(res, left + right + node.val, left + node.val, right + node.val, node.val)
            return max(left + node.val, right + node.val, node.val)
        dfs(root)
        return res


class Solution_2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right + node.val)
            return max(left + node.val, right + node.val, 0)
        dfs(root)
        return res

