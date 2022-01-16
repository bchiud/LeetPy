# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List

from common.listnode import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        divide and conquer
        time: n log(k) => takes n time to merge two sort lists, need to merge log(k) lists
        space: 1
        """
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]

        mid = 0 + (n - 0) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = curr = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 or l2

        return dummy.next


