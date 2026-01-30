# https://leetcode.com/problems/course-schedule/
# 30.01.2026


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for a, b in prerequisites:
            d[a].append(b)
        dd = {n: 0 for n in d}

        def dfs(n):
            if dd[n] == 1:
                return False
            dd[n] = 1
            for child in d[n]:
                if child in d and dd[child] != 2 and not dfs(child):
                    return False
            dd[n] = 2
            return True

        for n in d:
            if dd[n] != 2 and not dfs(n):
                return False
        return True

