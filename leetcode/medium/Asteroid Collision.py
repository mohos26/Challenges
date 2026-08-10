# https://leetcode.com/problems/asteroid-collision/
# 10.08.2026


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            if n > 0:
                stack.append(n)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(n):
                    stack.pop()
                if stack and stack[-1] == abs(n):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(n)
        return stack

