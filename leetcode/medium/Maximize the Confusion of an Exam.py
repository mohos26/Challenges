# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
# 18.01.2026


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        res = 0
        count_T = 0
        count_F = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                count_T += 1
            else:
                count_F += 1
            if r - l - max(count_T, count_F) + 1 <= k:
                res = max(res, r - l + 1)
            else:
                if answerKey[l] == 'T':
                    count_T -= 1
                else:
                    count_F -= 1
                l += 1
        return res

