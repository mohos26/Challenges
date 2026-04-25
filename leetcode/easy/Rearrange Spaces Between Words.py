# https://leetcode.com/problems/rearrange-spaces-between-words/
# 25.04.2026


class Solution:
    def reorderSpaces(self, text: str) -> str:
        lst = text.split()
        _len = text.count(' ')
        try:
            return (' ' * (_len // (len(lst) - 1))).join(lst) + ' ' * (_len % (len(lst) - 1))
        except:
            return ''.join(lst) + _len * ' '

