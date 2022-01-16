from common.listnode import ListNode


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0, head)

        left = 0
        while head:
            if left < m - 1:
                left += 1
            else:
                right = 0
                while right < n and head.next:
                    right += 1
                    head.next = head.next.next

                left = 0
            head = head.next

        return dummy.next



if __name__ == '__main__':
    s = Solution()
    assert s.deleteNodes(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10, ListNode(11, ListNode(12, ListNode(13))))))))))))),
                  2, 3) == ListNode(1, ListNode(2, ListNode(6, ListNode(7, ListNode(11, ListNode(12))))))