# https://leetcode.com/problems/evaluate-reverse-polish-notation
# 19.12.2025


class Solution:
    def eval(self, a, op, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '/':
            return int(a / b)
        elif op == '*':
            return a * b

    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for arg in tokens:
            if arg in '+*/-':
                b, a = stack.pop(), stack.pop()
                stack.append(self.eval(a, arg, b))
            else:
                stack.append(int(arg))
        return stack[0]

