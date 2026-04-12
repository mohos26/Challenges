# https://neetcode.io/problems/string-encode-and-decode/
# 12.04.2026


class Solution:

    def encode(self, strs: List[str]) -> str:
        return ":mohos:".join(strs) + ':end:' * bool(strs)

    def decode(self, s: str) -> List[str]:
        if ":end:" == s[-5:]:
            return s[:-5].split(":mohos:")
        return []

