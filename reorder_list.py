# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from common.listnode import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        split list in half
        reverse 2nd half
        attach as: 1st list, 2nd list, 1st list, 2nd list
        """
        if not head:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp

        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
