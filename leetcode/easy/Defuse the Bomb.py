# https://leetcode.com/problems/defuse-the-bomb
# 10.01.2025


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        window = sum(code[:k]) if k >= 0 else (sum(code[k:]))
        for i, n in enumerate(code):
            if k >= 0:
                window -= n
                window += code[(i+k)%len(code)]
                res.append(window)
            else:
                res.append(window)
                window += n
                window -= code[(len(code) + k + i) % len(code)]
        return res

