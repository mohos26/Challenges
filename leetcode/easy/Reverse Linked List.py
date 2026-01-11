# https://leetcode.com/problems/reverse-linked-list
# 30.10.2026


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst.reverse()
        if not lst:
            return None
        head = ListNode(lst[0])
        tmp = head
        for n in lst[1:]:
            tmp2 = ListNode(n)
            tmp.next = tmp2
            tmp = tmp2
        return head


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        while head:
            tmp = ListNode(head.val)
            tmp.next = res
            res = tmp
            head = head.next
        return res


class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        while head:
            res = ListNode(head.val, res)
            head = head.next
        return res

