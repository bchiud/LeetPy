from common.listnode import ListNode


class Solution:
    """
    time: n
    space: 1
    """
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        tortoise = head
        hare = head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True

        return False