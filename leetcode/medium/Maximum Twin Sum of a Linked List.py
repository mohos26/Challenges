# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# 27.09.2026


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        n = 1
        curr = head
        while curr:
            curr = curr.next
            n += 1
        lst = []
        i = n - 2
        curr = head
        while curr:
            if i >= n // 2:
                lst.append(curr.val)
            else:
                lst[i] += curr.val
            i -= 1
            curr = curr.next
        return max(lst)

