# https://leetcode.com/problems/group-anagrams/
# 09.09.2026


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            d[sorted_s] = d.get(sorted_s, []) + [s]
        return list(d.values())


# 20.10.2026
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return list(d.values())

