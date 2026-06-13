# https://leetcode.com/problems/capitalize-the-title
# 13.06.2026


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join((s.lower() if len(s) <= 2 else s.title()) for s in title.split())
