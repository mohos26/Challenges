# https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/
# 28.03.2026


class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        return 2 * comb(n-1, k) % (10**9 + 7)

