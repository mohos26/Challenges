# https://leetcode.com/problems/check-if-move-is-legal/
# 13.06.2026


class Solution:
    def checkMove(self, board: List[List[str]], rm: int, cm: int, color: str) -> bool:
        direction = (
            (0,1),
            (1,0),
            (0,-1),
            (-1,0),
            (1,1),
            (-1,-1),
            (-1,1),
            (1,-1),
        )
        target = 'W' if color == 'B' else 'B'
        for a, b in direction:
            i, j = rm + a, cm + b
            count = 1
            while 0 <= i < 8 and 0 <= j < 8 and board[i][j] == target:
                i += a
                j += b
                count += 1
            if 0 <= i < 8 and 0 <= j < 8 and board[i][j] == color and count >= 2:
                return True
        return False

