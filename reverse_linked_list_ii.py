# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common.listnode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None

        prev, curr = None, head
        while left > 1:
            prev, curr = curr, curr.next
            left -= 1
            right -= 1

        tail1, tail2 = prev, curr

        while right:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
            right -= 1

        if tail1:
            tail1.next = prev
        else:
            head = prev
        tail2.next = curr

        return head
