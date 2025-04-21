# https://edabit.com/challenge/wEDHiAcALvS2KuRBJ
# Very Hard
# 04.11.2024


class StackCalc:
    def __init__(self):
        self.res = []

    def run(self, instructions):
        for iteam in instructions.split():
            if iteam.isdigit():
                self.res.append(iteam)
            elif iteam in '+-*/':
                self.res = self.res[:-2] + [str(int(eval(self.res[-1] + iteam + self.res[-2])))]
            elif iteam == 'DUP':
                self.res.append(self.res[-1])
            elif iteam == 'POP':
                self.res = self.res[:-1]
            else:
                self.res = 'Invalid instruction: ' + iteam
                break

    def getValue(self):
        if not self.res:
            return 0
        if type(self.res) == str:
            return self.res
        return int(self.res[-1])
