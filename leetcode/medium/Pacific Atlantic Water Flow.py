# https://leetcode.com/problems/pacific-atlantic-water-flow/
# 27.01.2026


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        flag = None
        M, N = len(heights), len(heights[0])
        def dfs(i, j):
            if heights[i][j] < 0:
                flag.clear()
                return
            if heights[i][j] == float("inf"):
                return
            if (i == 0 or j == 0) and 1 in flag:
                flag.remove(1)
            if (i == M-1 or j == N-1) and 2 in flag:
                flag.remove(2)
            if not flag:
                return
            tmp, heights[i][j] = heights[i][j], float("inf")
            for a, b in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
                if 0 <= a < M and 0 <= b < N and tmp >= abs(heights[a][b]):
                    dfs(a, b)
                    if not flag:
                        heights[i][j] = tmp
                        return
            heights[i][j] = tmp

        for i in range(M):
            for j in range(N):
                flag = [1, 2]
                dfs(i, j)
                if not flag:
                    heights[i][j] *= -1
                    res.append((i, j))
                elif len(flag) == 2:
                    heights[i][j] = float("inf")
        return res

