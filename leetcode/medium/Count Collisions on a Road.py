# https://leetcode.com/problems/count-collisions-on-a-road/
# 14.01.2026


class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        stack = []
        for arg in directions:
            if arg == 'R':
                stack.append(arg)
                continue
            flag = bool(stack) or arg == 'S'
            while stack:
                aid = stack.pop()
                if aid == 'R' and arg == 'L':
                    res += 2
                    arg = 'S'
                elif aid == 'R' and arg == 'S':
                    res += 1
                elif aid == 'S' and arg == 'L':
                    res += 1
                    break
                else:
                    break
            if flag and not stack:
                stack.append('S')
        return res


class Solution:
    def countCollisions(self, directions: str) -> int:
        dirs = directions.lstrip("L").rstrip("R")
        return len(dirs) - dirs.count("S")

