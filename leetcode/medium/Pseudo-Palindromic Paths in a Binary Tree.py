# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# 30.04.2026


class Solution:
    def is_pseudo_palindromic(self, lst):
        odd_count = sum(n % 2 for n in lst)
        return odd_count == 0 or (odd_count == 1 and sum(lst) % 2)

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(lst, node):
            if not node:
                return 0
            res = 0
            lst[node.val-1] += 1
            if not node.left and not node.right:
                res += self.is_pseudo_palindromic(lst)
                lst[node.val-1] -= 1
                return res
            res += dfs(lst, node.left) + dfs(lst, node.right)
            lst[node.val-1] -= 1
            return res
        return dfs([0] * 9, root)

