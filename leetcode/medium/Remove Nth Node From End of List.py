# https://leetcode.com/problems/remove-nth-node-from-end-of-list
# 28.11.2026


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = n
        n = max(n+1, 3)
        tmp = head
        dumpy = ListNode()
        curr = dumpy
        stack = [curr]
        length = 0
        while tmp:
            curr.next = ListNode(tmp.val)
            curr = curr.next
            tmp = tmp.next
            stack.append(curr)
            if len(stack) > n:
                stack.pop(0)
            length += 1
        if length == 1:
            dumpy.next = None
        else:
            if N == 1:
                stack[-2].next = None
            else:
                stack[0].next = stack[2]
        return dumpy.next

