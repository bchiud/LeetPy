# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        pre_left = pre_right = dummy
        left = right = head

        for _ in range(k - 1):
            pre_left = pre_left.next
            left = left.next

        expected_tail = left
        while expected_tail.next:
            pre_right = pre_right.next
            right = right.next
            expected_tail = expected_tail.next

        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next

        return dummy.next
