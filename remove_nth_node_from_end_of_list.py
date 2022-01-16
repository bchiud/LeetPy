from common.listnode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        a b c d, 2
          l   r
        """
        if n == 0:
            return head

        # L is 1 index preceding item to be removed
        l, r = head, head
        for i in range(n):
            if not r:
                return head
            r = r.next

        # first item needs to be removed
        if not r:
            return head.next

        while r.next:
            l = l.next
            r = r.next
        l.next = l.next.next

        return head

        # fast = slow = head
        # for _ in range(n):
        #     if not fast:
        #         return head
        #     fast = fast.next
        # if not fast:
        #     return head.next
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next
        # slow.next = slow.next.next
        # return head


if __name__ == '__main__':
    s = Solution()

    i1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    e1 = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
    assert s.removeNthFromEnd(i1, 2) == e1

    i2 = ListNode(1)
    e2 = None
    assert s.removeNthFromEnd(i2, 1) == e2

    i3 = ListNode(1, ListNode(2))
    e3 = ListNode(1)
    assert s.removeNthFromEnd(i3, 1) == e3

    i4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    e4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert s.removeNthFromEnd(i4, 7) == e4
