from common.listnode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0

        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = val // 10
            curr.next = ListNode(val % 10)
            l1, l2, curr = l1.next if l1 else None, l2.next if l2 else None, curr.next

        return dummy.next

if __name__ == '__main__':
    s = Solution()
    assert s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))) \
           == ListNode(7, ListNode(0, ListNode(8)))
    assert s.addTwoNumbers(ListNode(0), ListNode(0)) == ListNode(0)
    assert s.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
                           ListNode(9, ListNode(9, ListNode(9, ListNode(9))))) \
           == ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))