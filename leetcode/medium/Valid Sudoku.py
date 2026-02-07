# https://leetcode.com/problems/valid-sudoku/
# 12.09.2025


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        for column in board:
            for i in range(9):
                rows[i].append(column[i])
            for arg in set(column):
                if arg != '.' and column.count(arg) > 1:
                    return False
        for row in rows:
            for arg in set(row):
                if arg != '.' and row.count(arg) > 1:
                    return False
        blocks = []
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                blocks.append([])
                for d in range(3):
                    blocks[-1] += board[i+d][j:j+3]
        for block in blocks:
            for arg in set(block):
                if arg != '.' and block.count(arg) > 1:
                    return False
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [defaultdict(int) for _ in range(9)]
        for column in board:
            for i in range(9):
                if column[i] != '.':
                    rows[i][column[i]] += 1
            column = Counter(column)
            if '.' in column:
                column.pop('.')
            if column and max(column.values()) > 1:
                return False
        for row in rows:
            if row and max(row.values()) > 1:
                return False
        blocks = []
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                blocks.append([])
                for d in range(3):
                    blocks[-1] += board[i+d][j:j+3]
        for block in blocks:
            block = Counter(block)
            if '.' in block:
                block.pop('.')
            if block and max(block.values()) > 1:
                return False
        return True


# 07.02.2026
class Solution:
    def ft_aid(self, hash_table, arg):
        if arg == '.':
            return True
        if arg in hash_table:
            return False
        hash_table.add(arg)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            column = set()
            box = set()
            for j in range(9):
                if not self.ft_aid(row, board[i][j]) or \
                   not self.ft_aid(column, board[j][i]) or \
                   not self.ft_aid(box, board[i//3*3 + j // 3][(i%3)*3 + j % 3]):
                    return False
        return True

