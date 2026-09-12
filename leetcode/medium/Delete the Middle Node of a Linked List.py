# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# 12.09.2026


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev is None:
            return None
        prev.next = slow.next
        return head

