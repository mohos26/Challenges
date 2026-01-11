# https://leetcode.com/problems/validate-binary-search-tree
# 15.12.2026


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q and p.val == q.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        return p == q or bool(p and q and p.val == q.val)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
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

    def bstInsert(self, root, node):
        while True:
            if root.val < node.val:
                if root.right:
                    root = root.right
                else:
                    root.right = node
                    break
            elif root.val > node.val:
                if root.left:
                    root = root.left
                else:
                    root.left = node
                    break
            else:
                return False
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lst = self.levelOrder(root)
        aid = TreeNode(lst[0][0])
        for arg in lst[1:]:
            for val in arg:
                if not self.bstInsert(aid, TreeNode(val)):
                    return False
        return self.isSameTree(root, aid)

class Solution_2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, curr, right):
            if not curr:
                return True
            if not left < curr.val < right:
                return False
            return dfs(left, curr.left, curr.val) and dfs(curr.val, curr.right, right)
        return dfs(float("-inf"), root, float("+inf"))

