# https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements
# 20.12.2026


class Solution: # Contest
    def minOperations(self, nums: List[int]) -> int:
        s = set(nums)
        C = Counter(nums)
        d = deque(nums)
        lenght = len(nums)
        res = 0
        while True:
            if len(s) == lenght:
                break
            for _ in range(3):
                n = d.popleft()
                C[n] -= 1
                if C[n] == 0:
                    s.remove(n)
                lenght -= 1
                if not d:
                    break
            res += 1
        return res


class Solution_2: # Cats7lives
    def minOperations(self, nums: List[int]) -> int:
        s = set()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in s:
                return ceil((i+1) / 3)
            s.add(nums[i])
        return 0

