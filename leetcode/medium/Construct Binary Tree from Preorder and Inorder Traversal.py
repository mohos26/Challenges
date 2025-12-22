# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# 23.12.2025


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(_inorder):
            if not _inorder:
                return
            n = preorder.pop(0)
            idx = _inorder.index(n)
            root = TreeNode(n)
            root.left = dfs(_inorder[:idx])
            root.right = dfs(_inorder[idx+1:])
            return root
        return dfs(inorder)


class Solution_2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(start, stop):
            if start >= stop:
                return
            n = preorder.pop(0)
            idx = inorder.index(n, start, stop)
            root = TreeNode(n)
            root.left = dfs(start, idx)
            root.right = dfs(idx+1, stop)
            return root
        return dfs(0, len(inorder))

