from common.listnode import ListNode


def reverseList(head: ListNode) -> ListNode:
    """
    1 -> 2 -> 3 -> 4
    1 <- 2    3 -> 4
    1 <- 2 <- 3    4
    1 <- 2 <- 3 <- 4
    """
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev