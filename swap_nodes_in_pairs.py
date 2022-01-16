from common.listnode import ListNode


def swapPairs(head: ListNode) -> ListNode:
    """
    time: n
    space: 1
    """
    pre = dummy = ListNode
    pre.next = head

    while pre.next and pre.next.next:
        first = pre.next
        second = pre.next.next

        pre.next, second.next, first.next = second, first, second.next
        pre = first

    return dummy.next


if __name__ == '__main__':
    d1 = ListNode(val=4)
    c1 = ListNode(val=3, next=d1)
    b1 = ListNode(val=2, next=c1)
    a1 = ListNode(val=1, next=b1)

    d2 = ListNode(val=3)
    c2 = ListNode(val=4, next=d2)
    b2 = ListNode(val=1, next=c2)
    a2 = ListNode(val=2, next=b2)

    print(a1.__str__())
    print(swapPairs(a1).__str__())

    # print(swapPairs(a1).__eq__(a2))
