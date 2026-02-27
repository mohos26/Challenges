# https://leetcode.com/problems/climbing-stairs/
# 26.07.2025

class Solution:
    def climbStairs(self, n: int) -> int:
        lst = [1, 1]
        while n > len(lst) - 1:
            lst.append(lst[-1] + lst[-2])
        return lst[-1]


# 27.02.2026
class Solution:
    def climbStairs(self, n: int) -> int:
        visited = {}
        def dfs(num):
            if num >= n:
                return num == n
            if num not in visited:
                visited[num] = dfs(num+1) + dfs(num+2)
            return visited[num]
        return dfs(0)


# 27.02.2026
class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        last = curr = 1
        for _ in range(n-1):
            last, curr = curr, last + curr
        return curr

