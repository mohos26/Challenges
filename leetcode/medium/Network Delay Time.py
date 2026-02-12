# https://leetcode.com/problems/network-delay-time/
# 12.02.2026


class Solution: # heap
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = {}
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append(v)
            time[(u,v)] = w
        heap = [(0, k)]
        visited = {k: 0}
        res = 0
        while heap:
            curr, source = heapq.heappop(heap)
            if curr != visited[source]:
                continue
            res = max(res, curr)
            for child in graph[source]:
                t = curr + time[(source, child)]
                if child not in visited or visited[child] > t:
                    heapq.heappush(heap, (t, child))
                    visited[child] = t
        for i in range(1, n+1):
            if i not in visited:
                return -1
        return res


class Solution: # deque
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        q = deque([(k, 0)])
        visited = {k: 0}
        while q:
            source, curr = q.popleft()
            if curr != visited[source]:
                continue
            for child, w in graph[source]:
                time = w + curr
                if child not in visited or visited[child] > time:
                    q.append((child, time))
                    visited[child] = time
        if len(visited) == n:
            return max(visited.values())
        return -1

