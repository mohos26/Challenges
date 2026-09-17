# https://leetcode.com/problems/odd-even-linked-list
# 17.09.2026


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        odd = curr_odd = ListNode()
        even = curr_even = ListNode()
        slow = head if head else None
        fast = head.next if head else None
        while slow:
            curr_even.next = ListNode(slow.val)
            curr_even = curr_even.next
            if not slow.next:
                break
            slow = slow.next.next

            curr_odd.next = ListNode(fast.val)
            curr_odd = curr_odd.next
            if not fast.next:
                break
            fast = fast.next.next

        curr_even.next = odd.next
        return even.next

