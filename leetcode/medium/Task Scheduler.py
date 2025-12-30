# https://leetcode.com/problems/task-scheduler/
# 29.12.2025


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        d = Counter(tasks)
        while d:
            lst = sorted(d, key=lambda key: d[key], reverse=True)
            for i in range(min(n+1, len(lst))):
                key = lst[i]
                d[key] -= 1
                if not d[key]:
                    d.pop(key)
            res += n + 1 if d else len(lst)
        return res


class Solution_2: # optimaze
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        lst = sorted(Counter(tasks).values())
        lst2 = deque()
        counter = 0
        while lst or lst2:
            res += 1
            counter += 1
            if lst:
                aid2 = lst.pop() - 1
                if aid2:
                    lst2.append(aid2)
            if counter > n:
                counter = 0
                while lst2:
                    bisect.insort(lst, lst2.pop())
        return res


class Solution_3: # heap
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        counter = 0
        lst = deque()
        heap = [-value for value in Counter(tasks).values()]
        heapq.heapify(heap)
        while heap or lst:
            res += 1
            counter += 1
            if heap:
                lst.append(1 + heapq.heappop(heap))
                if not lst[-1]:
                    lst.pop()
            if counter > n:
                counter = 0
                while lst:
                    heapq.heappush(heap, lst.pop())
        return res

