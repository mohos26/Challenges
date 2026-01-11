# https://leetcode.com/problems/valid-parentheses
# 23.07.2026


class Solution:
    d = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    def isValid(self, s: str) -> bool:
        lst = []
        for arg in s:
            if arg in "({[":
                lst.append(arg)
            elif lst and arg == self.d[lst[-1]]:
                lst = lst[:-1]
            else:
                return False
        return not lst


# 19.10.2026
class Solution:
    d = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    def isValid(self, s: str) -> bool:
        lst = []
        for arg in s:
            if arg in self.d:
                lst.append(arg)
            elif lst and arg == self.d[lst[-1]]:
                lst.pop()
            else:
                return False
        return not lst

