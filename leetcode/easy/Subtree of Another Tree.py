# https://leetcode.com/problems/subtree-of-another-tree/
# 13.12.2026


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q and p.val == q.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        return p == q or bool(p and q and p.val == q.val)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        return root and bool(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

