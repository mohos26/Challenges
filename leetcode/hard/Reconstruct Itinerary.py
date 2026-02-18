# https://leetcode.com/problems/reconstruct-itinerary/
# 18.02.2026


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(deque)
        for _from, to in sorted(tickets, key=lambda l: l[1]):
            graph[_from].append(to)
        res = []
        def dfs(parent):
            children = graph[parent]
            while children:
                child = children.popleft()
                dfs(child)
            res.append(parent)

        dfs("JFK")

        return res[::-1] if res else ["JFK"]

