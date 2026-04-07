# https://leetcode.com/problems/product-of-array-except-self/
# 11.09.2025


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, res = [1], [1], []
        for i in range(len(nums) - 1):
            prefix.append(prefix[-1] * nums[i])
            suffix.insert(0, suffix[0] * nums[-i-1])
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res


# 07.04.2026
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        curr = 1
        for n in nums:
            prefix.append(curr)
            curr *= n
        postfix = []
        curr = 1
        for n in nums[::-1]:
            postfix.append(curr)
            curr *= n
        postfix.reverse()
        res = []
        for a, b in zip(prefix, postfix):
            res.append(a * b)
        return res

