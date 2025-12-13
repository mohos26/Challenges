# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
# 13.12.2025


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def dfs(root, p, q):
            nonlocal res
            if root is None:
                if p is None and q is None:
                    return 2
                elif p is None or q is None:
                    return 1
                return 0
            p_base, q_base = p, q
            if root == p:
                p = None
            elif root == q:
                q = None
            left, right = dfs(root.left, p, q), dfs(root.right, p, q)
            aid = min(2, left + right)
            if ((left and right) or ((left or right) and (p_base != p or q_base != q))):
                res = root
            return aid
        dfs(root, p, q)
        return res

