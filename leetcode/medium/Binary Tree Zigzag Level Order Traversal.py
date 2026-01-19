# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# 19.01.2026


class Solution:
    def maxDeept(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDeept(root.left), self.maxDeept(root.right))

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [[] for _ in range(self.maxDeept(root))]
        def dfs(node, deept):
            if not node:
                return
            res[deept].append(node.val)
            dfs(node.left, deept+1)
            dfs(node.right, deept+1)
        dfs(root, 0)
        for i in range(len(res)):
            if i % 2:
                res[i].reverse()
        return res

