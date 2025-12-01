# https://leetcode.com/problems/reverse-string
# 19.10.2025


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

class Solution_2:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

