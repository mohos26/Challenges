# https://leetcode.com/problems/clone-graph/
# 21.01.2026


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None
        d = {}

        def dfs(node):
            if node in d:
                return d[node]
            new_node = Node(node.val)
            d[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node

        return dfs(node)


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None
        d = {}

        def bfs(node):
            lst = deque()
            lst.append(node)
            d[node] = Node(node.val)
            while lst:
                arg = lst.popleft()
                curr = d[arg]
                for neighbor in arg.neighbors:
                    if neighbor not in d:
                        d[neighbor] = Node(neighbor.val)
                        lst.append(neighbor)
                    curr.neighbors.append(d[neighbor])
            return d[node]

        return bfs(node)

