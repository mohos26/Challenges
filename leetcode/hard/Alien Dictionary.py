# https://neetcode.io/problems/foreign-dictionary
# 26.02.2026


class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, target):
        if target not in self.parent:
            self.parent[target] = target
        if target != self.parent[target]:
            self.parent[target] = self.find(self.parent[target])
        return self.parent[target]


    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        self.parent[rb] = ra

    def base(self):
        return self.find(list(self.parent.keys())[0])


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        last = words[0]
        for word in words[1:]:
            for a, b in zip(last, word):
                if a != b:
                    if b not in graph[a]:
                        graph[a].append(b)
                    break
            else:
                if len(last) > len(word): # like: app, apple
                    return ""
            last = word

        res = ""
        visited = defaultdict(int)
        def dfs(letter):
            if visited[letter] == 2:
                return True
            if visited[letter] == 1:
                return False
            visited[letter] = 1
            if letter in graph:
                for child in graph[letter]:
                    if not dfs(child):
                        return False
            nonlocal res
            res += letter
            visited[letter] = 2
            return True

        dsu = DSU()
        for parent, childs in graph.items():
            for child in childs:
                dsu.union(parent, child)

        if graph and not dfs(dsu.base()):
            return ''

        res = res[::-1]
        for word in words:
            for letter in word:
                if letter in visited:
                    continue
                res += letter
                visited[letter] = 2
        return res


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        last = words[0]
        for word in words[1:]:
            for a, b in zip(last, word):
                if a != b:
                    if b not in graph[a]:
                        graph[a].append(b)
                    break
            else:
                if len(last) > len(word): # like: app, apple
                    return ""
            last = word

        res = ""
        visited = defaultdict(int)
        def dfs(letter):
            if visited[letter] == 2:
                return True
            if visited[letter] == 1:
                return False
            visited[letter] = 1
            if letter in graph:
                for child in graph[letter]:
                    if not dfs(child):
                        return False
            nonlocal res
            res += letter
            visited[letter] = 2
            return True

        for letter in graph:
            if not dfs(letter):
                return ''

        res = res[::-1]
        for word in words:
            for letter in word:
                if letter in visited:
                    continue
                res += letter
                visited[letter] = 2
        return res

