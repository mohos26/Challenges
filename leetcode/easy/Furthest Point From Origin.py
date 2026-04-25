# https://leetcode.com/problems/furthest-point-from-origin/
# 25.04.2026


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        res = 0
        _max = 'L' if moves.count('L') > moves.count('R') else 'R'
        for arg in moves:
            if arg == '_':
                arg = _max
            res += 1 if arg == 'R' else -1
        return abs(res)

