# https://leetcode.com/problems/smallest-subsequence
# 11.01.2026


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        hash_table = set()
        d = {s[i]:i for i in range(len(s))}
        for i in range(len(s)):
            letter = s[i]
            if letter in hash_table:
                continue
            while stack and stack[-1] > letter and d[stack[-1]] > i:
                hash_table.remove(stack.pop())
            hash_table.add(letter)
            stack.append(letter)
        return ''.join(stack)

