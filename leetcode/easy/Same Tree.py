# https://leetcode.com/problems/same-tree
# 11.12.2026


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q and p.val == q.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        return p == q or bool(p and q and p.val == q.val)

