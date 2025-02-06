# https://edabit.com/challenge/pyKqBxTT9BMLxTFeZ
# Hard
# 10.09.2024


class Menu:
    def __init__(self, lst):
        self.current = 0
        self.max_index = len(lst) - 1
        self.lst = [[lst[0]]] + lst[1:]

    def display(self):
        return str(self.lst)

    def to_the_right(self):
        if self.current == self.max_index:
            self.current = 0
            self.lst = [[self.lst[0]]] + self.lst[1:-1] + self.lst[-1]
        else:
            self.lst = self.lst[:self.current] + self.lst[self.current] + [[self.lst[self.current+1]]] + self.lst[self.current+2:]
            self.current += 1
