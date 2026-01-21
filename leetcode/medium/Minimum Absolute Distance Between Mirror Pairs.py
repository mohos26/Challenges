# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/
# 21.01.2026


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d = defaultdict(deque)
        for i, n in enumerate(nums):
            d[n].append(i)
        res = float("inf")
        for i in range(len(nums) - 1):
            a = int(str(nums[i])[::-1])
            if a in d:
                while d[a]:
                    if d[a][0] > i:
                        res = min(res, d[a][0] - i)
                        break
                    else:
                        d[a].popleft()
        return res if res != float("inf") else -1


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d = {}
        res = float("inf")
        for i in range(len(nums)):
            n = nums[i]
            if n in d:
                res = min(res, i - d[n])
            d[int(str(nums[i])[::-1])] = i
        return res if res != float("inf") else -1

