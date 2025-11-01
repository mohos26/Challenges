# https://leetcode.com/problems/sliding-window-maximum
# 01.11.2025


class Solution_wrong: # Time out
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for left, right in zip(range(len(nums)-k+1), range(k-1, len(nums))):
            if left:
                l.append(nums[right])
            else:
                l = nums[left:right+1]
            l.sort()
            res.append(l[-1])
            l.remove(nums[left])
        return res


class Solution_wrong2: # Time out but optimiz
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_v = None
        for left, right in zip(range(len(nums)-k+1), range(k-1, len(nums))):
            if max_v == None:
                max_v = max(nums[left:right+1])
                max_i = nums[left:right+1].index(max_v)
            elif nums[right] > max_v:
                max_v = nums[right]
                max_i = k-1
            res.append(max_v)
            if not max_i:
                max_v = None
            max_i -= 1
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        start = True
        for left, right in zip(range(len(nums)-k+1), range(k-1, len(nums))):
            if queue and queue[0] < left:
                queue.popleft()
            if start:
                for i in range(left, right+1):
                    if not queue or nums[queue[-1]] > nums[i]:
                        queue.append(i)
                    else:
                        while queue and nums[queue[-1]] < nums[i]:
                            queue.pop()
                        queue.append(i)
                start = False
            else:
                while queue and nums[queue[-1]] < nums[right]:
                    queue.pop()
                queue.append(right)
            res.append(nums[queue[0]])
        return res

