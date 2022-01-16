from common.listnode import ListNode


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    time: n + m
    space: n + m
    """
    # dummy = ListNode()
    # if not l1 and not l2:
    #     return None
    # elif l1 and not l2:
    #     dummy.next = l1
    #     l1 = l1.next
    # elif not l1 and l2:
    #     dummy.next = l2
    #     l2 = l2.next
    # elif l1.val <= l2.val:
    #     dummy.next = l1
    #     l1 = l1.next
    # else:
    #     dummy.next = l2
    #     l2 = l2.next
    # dummy.next.next = mergeTwoLists(l1, l2)
    # return dummy.next

    """
    time: n + m
    space: 1
    """
    dummy = curr = ListNode()

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 if l1 else l2

    return dummy.next



