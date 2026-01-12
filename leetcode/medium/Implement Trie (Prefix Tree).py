# https://leetcode.com/problems/implement-trie-prefix-tree
# 12.01.2026


class Trie:
    def __init__(self):
        self.hash_table = set()

    def insert(self, word: str) -> None:
        self.hash_table.add(word)

    def search(self, word: str) -> bool:
        return word in self.hash_table

    def startsWith(self, prefix: str) -> bool:
        for word in self.hash_table:
            if word.startswith(prefix):
                return True
        return False


class Trie_2:
    def __init__(self):
        self.lst = [None] * 26

    def insert(self, word: str) -> None:
        lst = self.lst
        for letter in word:
            if not lst[ord(letter) - ord('a')]:
                lst[ord(letter) - ord('a')] = [None] * 26 + [False]
            lst = lst[ord(letter) - ord('a')]
        lst[-1] = True

    def search(self, word: str) -> bool:
        lst = self.lst
        for letter in word:
            if lst[ord(letter) - ord('a')]:
                lst = lst[ord(letter) - ord('a')]
            else:
                return False
        return lst[-1]

    def startsWith(self, prefix: str) -> bool:
        lst = self.lst
        for letter in prefix:
            if lst[ord(letter) - ord('a')]:
                lst = lst[ord(letter) - ord('a')]
            else:
                return False
        return True


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie_3:
    def __init__(self):
        self.lst = TrieNode()

    def insert(self, word: str) -> None:
        lst = self.lst
        for letter in word:
            idx = ord(letter) - 97
            if not lst.children[idx]:
                lst.children[idx] = TrieNode()
            lst = lst.children[idx]
        lst.end = True

    def search(self, word: str) -> bool:
        lst = self.lst
        for letter in word:
            idx = ord(letter) - 97
            if lst.children[idx]:
                lst = lst.children[idx]
            else:
                return False
        return lst.end

    def startsWith(self, prefix: str) -> bool:
        lst = self.lst
        for letter in prefix:
            idx = ord(letter) - 97
            if lst.children[idx]:
                lst = lst.children[idx]
            else:
                return False
        return True

