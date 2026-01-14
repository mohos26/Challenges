# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# 14.01.2026


class TrieNode():
    def __init__(self):
        self.lst = [None] * 26
        self.end = False

class WordDictionary:
    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        trie = self.trie
        for letter in word:
            idx = ord(letter) - 97
            if not trie.lst[idx]:
                trie.lst[idx] = TrieNode()
            trie = trie.lst[idx]
        trie.end = True

    def search(self, word: str) -> bool:
        def dfs(trie, i):
            if i == len(word):
                return trie.end
            if word[i] == '.':
                for arg in trie.lst:
                    if arg and dfs(arg, i + 1):
                        return True
            elif trie.lst[ord(word[i]) - 97] and dfs(trie.lst[ord(word[i]) - 97], i + 1):
                return True
            return False
        return dfs(self.trie, 0)

