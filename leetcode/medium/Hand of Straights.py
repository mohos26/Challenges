# https://leetcode.com/problems/hand-of-straights/
# 28.05.2026


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        d = Counter(hand)
        for n in d:
            if d[n] == 0:
                continue
            start = n
            while d[start - 1] != 0:
                start -= 1
            for nn in range(start, n + 1):
                while d[nn] != 0:
                    for m in range(nn, nn + groupSize):
                        if d[m] == 0:
                            return False
                        d[m] -= 1
        return not any(d.values())
