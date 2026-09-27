# https://leetcode.com/problems/leaf-similar-trees/
# 27.09.2026


class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        lst = []
        def dfs(node):
            if not node:
                return
            if node.left is node.right:
                lst.append(node.val)
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root1)
        lst1 = lst.copy()
        lst.clear()
        dfs(root2)
        return lst1 == lst

