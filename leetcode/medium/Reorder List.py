# https://leetcode.com/problems/reorder-list
# 25.11.2025


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        tmp = head
        while tmp:
            lst.append(tmp.val)
            tmp = tmp.next
        l1, l2 = lst[:len(lst)//2], lst[:len(lst)//2-1:-1]
        for a, b in zip(l1, l2):
            head.val = a
            head.next.val = b
            head = head.next.next
        if len(l2) > len(l1):
            head.val = l2[-1]

