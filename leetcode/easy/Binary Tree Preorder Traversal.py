# https://leetcode.com/problems/binary-tree-preorder-traversal
# 23.12.2025


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        def dfs(node):
            if not node:
                return
            preorder.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return preorder

