# https://leetcode.com/problems/unique-number-of-occurrences/
# 01.08.2026


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        return len(d) == len(set(d.values()))

