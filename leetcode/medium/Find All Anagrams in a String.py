# https://leetcode.com/problems/find-all-anagrams-in-a-string
# 08.12.2025


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        base = Counter(p)
        tmp = defaultdict(int)
        for i, letter in enumerate(s):
            if i < len(p) - 1:
                tmp[letter] += 1
            else:
                tmp[letter] += 1
                if tmp == base:
                    res.append(i - len(p) + 1)
                tmp[s[i - len(p) + 1]] -= 1
                if not tmp[s[i - len(p) + 1]]:
                    tmp.pop(s[i - len(p) + 1])
        return res


class Solution_2:
    def index(self, letter):
        return ord(letter) - ord('a')

    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        base = [0] * 26
        for letter in p:
            base[self.index(letter)] += 1
        tmp = [0] * 26
        for i, letter in enumerate(s):
            if i < len(p) - 1:
                tmp[self.index(letter)] += 1
            else:
                tmp[self.index(letter)] += 1
                if tmp == base:
                    res.append(i - len(p) + 1)
                tmp[self.index(s[i - len(p) + 1])] -= 1
        return res


