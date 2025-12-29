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

