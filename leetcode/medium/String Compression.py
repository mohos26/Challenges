# https://leetcode.com/problems/string-compression
# 16.12.2026


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 1
        count = 1
        while i < len(chars):
            if count and chars[i] == chars[i-1]:
                count += 1
                chars.pop(i)
            elif count > 1:
                for n in str(count):
                    chars.insert(i, n)
                    i += 1
                count = 0
            else:
                count = 1
                i += 1
        if count > 1:
            chars.extend(list(str(count)))

