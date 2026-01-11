# https://leetcode.com/problems/merge-k-sorted-lists/
# 01.12.2026


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dumpy = ListNode()
        curr = dumpy
        while True:
            min_v = float("inf")
            indices = []
            for i in range(len(lists)):
                if lists[i]:
                    if min_v == lists[i].val:
                        indices.append(i)
                    elif min_v > lists[i].val:
                        min_v = lists[i].val
                        indices = [i]
            if not indices:
                break
            for i in indices:
                while lists[i] and lists[i].val == min_v:
                    curr.next = ListNode(min_v)
                    curr = curr.next
                    lists[i] = lists[i].next
        return dumpy.next

