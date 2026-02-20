# https://leetcode.com/problems/merge-two-sorted-lists
# 24.11.2026


class Solution:
    def add_back(self, val):
        if not self.result:
            self.result = ListNode(val)
            return
        tmp = self.result
        if self.result.val > val:
            self.result = ListNode(val)
            self.result.next = tmp
            return
        while tmp.next:
            if tmp.next.val > val:
                tmp2 = tmp
                tmp.next, tmp.next.next = ListNode(val), tmp.next
                return
            tmp = tmp.next
        tmp.next = ListNode(val)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.result = None
        while list1 or list2:
            if list1:
                self.add_back(list1.val)
                list1 = list1.next
            if list2:
                self.add_back(list2.val)
                list2 = list2.next
        return self.result


# 20.02.2026
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dumpy = ListNode()
        curr = dumpy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
        while list1:
            curr.next = ListNode(list1.val)
            list1 = list1.next
            curr = curr.next
        while list2:
            curr.next = ListNode(list2.val)
            list2 = list2.next
            curr = curr.next
        return dumpy.next

