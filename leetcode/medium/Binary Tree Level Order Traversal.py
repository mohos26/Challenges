# https://leetcode.com/problems/binary-tree-level-order-traversal
# 14.12.2026


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [[] for _ in range(self.maxDepth(root))]
        def dfs(node, depth):
            if not node:
                return
            nonlocal res
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            res[depth].append(node.val)
        dfs(root, 0)
        return res

