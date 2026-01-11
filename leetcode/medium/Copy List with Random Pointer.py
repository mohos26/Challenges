# https://leetcode.com/problems/copy-list-with-random-pointer
# 28.11.2026


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dumpy = Node(0)
        curr = dumpy
        tmp = head
        d = {}
        while tmp:
            curr.next = Node(tmp.val)
            curr = curr.next
            d[tmp] = curr
            tmp = tmp.next
        curr = dumpy.next
        tmp = head
        while curr:
            if tmp.random:
                curr.random = d[tmp.random]
            curr = curr.next
            tmp = tmp.next
        return dumpy.next

