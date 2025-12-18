# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# 18.12.2025


class Solution:
    def binary_insert(self, lst, val):
        left, right = 0, len(lst)
        while left < right:
            medium = left + (right - left) // 2
            if lst[medium] > val:
                right = medium
            else:
                left = medium + 1
        lst.insert(right, val)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node):
            if not node:
                return
            self.binary_insert(res, node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res[k-1]

