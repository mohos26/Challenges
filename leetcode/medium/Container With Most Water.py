# https://leetcode.com/problems/container-with-most-water/
# 17.09.2026


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        x, y = 0, len(height) - 1
        while x < y:
            res = max(res, (y-x) * min(height[x], height[y]))
            if height[x] > height[y]:
                y -= 1
            else:
                x += 1
        return res


# 11.02.2026
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            res = max(res, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res

