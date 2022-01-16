from common.listnode import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head

        n = 1
        curr = head
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head

        moves = n - (k % n) - 1
        print(f'{n} {k} {moves}')
        curr = head
        for _ in range(moves):
            curr = curr.next
        dummy = ListNode(0, curr.next)
        curr.next = None

        return dummy.next


if __name__ == '__main__':
    s = Solution()
    # assert s.rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2) \
    #        == ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3)))))
    assert s.rotateRight(ListNode(0, ListNode(1, ListNode(2))), 4) == ListNode(2, ListNode(0, ListNode(1)))
