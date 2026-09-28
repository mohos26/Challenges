# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# 28.09.2026


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, _max):
            if not node:
                return 0
            _max = max(node.val, _max)
            return (node.val >= _max) + dfs(node.left, _max) + dfs(node.right, _max)
        return dfs(root, float("-inf"))

