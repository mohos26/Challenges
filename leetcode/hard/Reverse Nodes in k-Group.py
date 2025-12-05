#
# 05.12.2025


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                if not kth.next:
                    return dummy.next
                kth = kth.next
            group_next = kth.next
            prev, curr = group_next, group_prev.next
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            temp = group_prev.next
            group_prev.next = prev
            group_prev = temp

