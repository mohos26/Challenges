# https://leetcode.com/problems/serialize-and-deserialize-binary-tree
# 23.12.2025


class Codec:
    def serialize(self, root):
        preorder = deque()
        def dfs(node):
            if not node:
                preorder.append('.')
                return
            preorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ' '.join(preorder)

    def deserialize(self, data):
        lst = iter(data.split())
        def dfs():
            val = next(lst)
            if val == '.':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

