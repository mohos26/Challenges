# https://leetcode.com/problems/valid-parenthesis-string/
# 29.05.2026


class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for arg in s:
            if arg in '(*':
                stack.append(arg)
            else:
                tmp = 0
                while stack and stack[-1] == '*':
                    stack.pop()
                    tmp += 1
                if stack:
                    stack.pop()
                elif tmp:
                    tmp -= 1
                else:
                    return False
                stack.extend(tmp * ['*'])
        res = 0
        for arg in stack:
            if arg == '(':
                res += 1
            elif res:
                res -= 1
        return res == 0
