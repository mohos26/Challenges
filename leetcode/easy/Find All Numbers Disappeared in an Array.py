# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
# 19.12.2026


class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution: # Double linked list
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        dumpy = Node()
        curr = dumpy
        for n in range(1, len(nums)+1):
            curr.next = Node(n, prev=curr)
            curr = curr.next
            d[n] = curr
        for n in nums:
            if n in d:
                prev = d[n].prev
                _next = d[n].next
                prev.next = _next
                if _next:
                    _next.prev = prev
                d.pop(n)
        res = []
        curr = dumpy.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


class Solution_2: # hash_table
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = set(range(1, len(nums)+1))
        for n in nums:
            if n in d:
                d.remove(n)
        return list(d)


class Solution_3: # hash_table (optimize)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        d = set(nums)
        for n in range(1, len(nums)+1):
            if n not in d:
                res.append(n)
        return res

