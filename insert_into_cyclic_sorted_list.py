"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

from common.listnode import ListNode as Node


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            a = Node(insertVal)
            a.next = a
            return a

        """
        1) prev <= insert <= curr
        2) prev > curr AND (prev <= insert OR insert <= curr)
        3) all prev == curr AND insert != curr
        """
        prev, curr = head, head.next
        toInsert = False
        while not toInsert:
            if prev.val <= insertVal <= curr.val:  # 1
                toInsert = True
            elif prev.val > curr.val:
                if prev.val <= insertVal or insertVal <= curr.val:  # 2
                    toInsert = True

            if toInsert:
                break

            prev, curr = prev.next, curr.next
            if prev == head:  # 3
                break

        prev.next = Node(insertVal, curr)
        return head
