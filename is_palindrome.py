# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common.listnode import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        lastNodeOfFirstHalf = self.lastNodeOfFirstHalf(head)
        firstNodeOfSecondHalf = self.reverse(lastNodeOfFirstHalf.next)

        result = True
        l, r = head, firstNodeOfSecondHalf
        while result and r:
            if l.val != r.val:
                result = False
            l = l.next
            r = r.next

        lastNodeOfFirstHalf.next = self.reverse(firstNodeOfSecondHalf)
        return result

    def reverse(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    def lastNodeOfFirstHalf(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))) == True
    assert s.isPalindrome(ListNode(1, ListNode(2))) == False
