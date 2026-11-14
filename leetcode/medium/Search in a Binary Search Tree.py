# https://leetcode.com/problems/search-in-a-binary-search-tree/
# 14.11.2026


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST((root.left if root.val > val else root.right), val)

