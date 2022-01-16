from typing import Optional

from common.listnode import ListNode


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        time: n
        space: 1

        val:    0   1   2   -3  3   1
        total:  0   1   3   0   3   1
            =>  0   ->  ->  ->  3   1
        """
        dummy = ListNode(0, head)
        total_to_node = {
            0: dummy
        }

        curr = head
        curr_total = 0
        while curr:
            curr_total += curr.val
            total_to_node[curr_total] = curr
            curr = curr.next

        curr = dummy
        curr_total = 0
        while curr:
            curr_total += curr.val
            curr.next = total_to_node[curr_total].next
            curr = curr.next

        return dummy.next