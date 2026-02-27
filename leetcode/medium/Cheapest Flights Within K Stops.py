# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# 27.02.2026


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for _from, to, price in flights:
            graph[_from].append((to, price))
        pd = deque([(src, 0)])
        visited = {src: 0}
        for _ in range(k+1):
            if not pd:
                break
            for _ in range(len(pd)):
                city, cost = pd.popleft()
                if city == dst:
                    continue
                for destination, price in graph[city]:
                    if destination in visited and visited[destination] < cost + price:
                        continue
                    pd.append((destination, cost + price))
                    visited[destination] = cost + price
        if dst in visited:
            return visited[dst]
        return -1

