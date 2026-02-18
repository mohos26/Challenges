# https://leetcode.com/problems/number-of-prefix-connected-groups/
# 18.02.2026


class Solution: # contest
    def prefixConnected(self, words: List[str], k: int) -> int:
        res = 0
        d = defaultdict(int)
        for word in words:
            if len(word) < k:
                continue
            d[word[:k]] += 1
            if d[word[:k]] == 2:
                res += 1
        return res

