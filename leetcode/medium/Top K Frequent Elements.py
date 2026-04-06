# https://leetcode.com/problems/top-k-frequent-elements/
# 09.09.2025


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        res = []
        for n, count in sorted(list(d.items()), key=lambda l: l[1], reverse=True)[:k]:
            res.append(n)
        return res


# 06.04.2026
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [ll[0] for ll in Counter(nums).most_common(k)]

