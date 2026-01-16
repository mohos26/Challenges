# https://leetcode.com/problems/word-search-ii
# 16.01.2026


class TrieNode():
    def __init__(self):
        self.lst = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            tmp = trie
            for letter in word:
                if letter not in tmp.lst:
                    tmp.lst[letter] = TrieNode()
                tmp = tmp.lst[letter]
            tmp.end = True
        res = []
        def dfs(trie, s, i, j):
            if trie.end:
                trie.end = False # skip repetation
                res.append(s)
            for a, b in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] in trie.lst:
                    tmp, board[a][b] = board[a][b], None
                    dfs(trie.lst[tmp], s + tmp, a, b)
                    board[a][b] = tmp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.lst:
                    tmp, board[i][j] = board[i][j], None
                    dfs(trie.lst[tmp], tmp, i, j)
                    board[i][j] = tmp
        return res

