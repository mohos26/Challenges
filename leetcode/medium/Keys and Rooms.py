# https://leetcode.com/problems/keys-and-rooms/
# 15.11.2026


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in rooms[node]:
                dfs(n)
        dfs(0)
        return len(visited) == len(rooms)

