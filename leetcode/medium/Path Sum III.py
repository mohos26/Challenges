class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        memo = set()
        def dfs(node, curr):
            if not node:
                return 0
            curr += node.val
            res = int(targetSum == curr) + dfs(node.left, curr) + dfs(node.right, curr)
            if not (node, node.left) in memo:
                res += dfs(node.left, 0)
                memo.add((node, node.left))
            if not (node, node.right) in memo:
                res += dfs(node.right, 0)
                memo.add((node, node.right))
            return  res
        return dfs(root, 0)

