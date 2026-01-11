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

