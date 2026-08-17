# https://leetcode.com/problems/dota2-senate/
# 17.08.2026


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        tmp = ''
        r = d = 0
        senate = deque(senate)
        len_r, len_d = senate.count('R'), senate.count('D')
        while senate:
            s = senate.popleft()
            if s == 'R':
                len_r -= 1
                if r == 0:
                    d += 1
                    if len_d != 0:
                        len_r += 1
                        senate.append(s)
                else:
                    r -= 1
            elif s == 'D':
                len_d -= 1
                if d == 0:
                    r += 1
                    if len_r != 0:
                        senate.append(s)
                        len_d += 1
                else:
                    d -= 1
        if r == 0:
            return "Radiant"
        return "Dire"

