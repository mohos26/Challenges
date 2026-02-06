# https://leetcode.com/problems/word-ladder/
# 06.20.2026


class Trie:
    def __init__(self):
        self.letters = {}

    def wildcard(self, word):
        res = []
        def dfs(i, curr, w):
            if i == len(word):
                res.append(w)
                return

            if word[i] == '*':
                for letter in curr.letters:
                    dfs(i+1, curr.letters[letter], w + letter)
            elif word[i] in curr.letters:
                dfs(i+1, curr.letters[word[i]], w + word[i])
        dfs(0, self, '')
        return res


class Solution: # trie + wildcard dfs + build graph + bfs multi source
    def ft_aid(self, w1, w2):
        res = 0
        for a, b in zip(w1, w2):
            if a != b:
                res += 1
        return res == 1

    def ft_aid2(self, word):
        res = []
        for i in range(len(word)):
            res.append(word[:i] + '*' + word[i+1:])
        return res

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        trie = Trie()
        for word in wordList + [beginWord]:
            curr = trie
            for letter in word:
                if letter not in curr.letters:
                    curr.letters[letter] = Trie()
                curr = curr.letters[letter]

        graph = defaultdict(set)

        for word in wordList + [beginWord]:
            for arg in self.ft_aid2(word):
                for arg2 in trie.wildcard(arg):
                    if word != arg2:
                        graph[word].add(arg2)

        if endWord not in graph:
            return 0

        def bfs(lst, d, dd):
            while True:
                arg = lst.popleft()
                if arg is None:
                    break
                for arg2 in graph[arg]:
                    if d[arg2]:
                        continue
                    if dd[arg2]:
                        return True
                    d[arg2] = True
                    lst.append(arg2)
            return False

        begin = defaultdict(bool)
        begin[beginWord] = True
        end = defaultdict(bool)
        end[endWord] = True

        q_begin = deque([beginWord])
        q_end = deque([endWord])

        res = 2

        while True:
            q_begin.append(None)
            q_end.append(None)

            if bfs(q_begin, begin, end):
                return res
            res += 1
            if bfs(q_end, end, begin):
                return res
            res += 1
            if not q_begin or not q_end:
                break

        return 0


class Trie:
    def __init__(self):
        self.letters = {}

    def wildcard(self, word):
        res = []
        def dfs(i, curr, w):
            if i == len(word):
                res.append(w)
                return

            if word[i] == '*':
                for letter in curr.letters:
                    dfs(i+1, curr.letters[letter], w + letter)
            elif word[i] in curr.letters:
                dfs(i+1, curr.letters[word[i]], w + word[i])
        dfs(0, self, '')
        return res


class Solution: # trie + wildcard dfs + bfs multi source

    def ft_aid2(self, trie, word):
        aid = []
        for i in range(len(word)):
            aid.append(word[:i] + '*' + word[i+1:])
        res = []
        for wild in aid:
            res.extend(trie.wildcard(wild))
        return res

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        trie = Trie()
        for word in wordList + [beginWord]:
            curr = trie
            for letter in word:
                if letter not in curr.letters:
                    curr.letters[letter] = Trie()
                curr = curr.letters[letter]

        def bfs(lst, d, dd):
            while True:
                arg = lst.popleft()
                if arg is None:
                    break
                for arg2 in self.ft_aid2(trie, arg):
                    if d[arg2]:
                        continue
                    if dd[arg2]:
                        return True
                    d[arg2] = True
                    lst.append(arg2)
            return False

        begin = defaultdict(bool)
        begin[beginWord] = True
        end = defaultdict(bool)
        end[endWord] = True

        q_begin = deque([beginWord])
        q_end = deque([endWord])

        res = 2

        while True:
            q_begin.append(None)
            q_end.append(None)

            if bfs(q_begin, begin, end):
                return res
            res += 1
            if bfs(q_end, end, begin):
                return res
            res += 1
            if not q_begin or not q_end:
                break

        return 0

