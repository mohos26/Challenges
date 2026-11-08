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


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        res = 0
        memo = defaultdict(int)
        memo[0] = 1
        def dfs(node, total):
            nonlocal res
            if not node:
                return
            total += node.val
            if memo[total - targetSum]:
                res += memo[total - targetSum]
            memo[total] += 1
            dfs(node.left, total)
            dfs(node.right, total)
            memo[total] -= 1
        dfs(root, 0)
        return res

