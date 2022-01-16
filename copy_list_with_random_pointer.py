class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        cur1 = head
        while cur1 is not None:
            cur1.next = Node(cur1.val, cur1.next, None)
            cur1 = cur1.next.next

        curr = head
        while curr is not None:
            curr = curr.next

        cur2 = head
        while cur2 is not None:
            cur2.next.random = cur2.random.next if cur2.random else None
            cur2 = cur2.next.next

        dummy = Node(0)
        dummy.next = head
        origCurr = head
        copyCurr = dummy
        while origCurr is not None:
            origCurr.next, copyCurr.next = origCurr.next.next, copyCurr.next.next
            origCurr, copyCurr = origCurr.next, copyCurr.next

        return dummy.next

if __name__ == '__main__':
    a5 = Node(1, None, None)
    a4 = Node(10, a5)
    a3 = Node(11, a4)
    a2 = Node(13, a3)
    a1 = Node(7, a2)

    a1.random = None
    a2.random = a1
    a3.random = a5
    a4.random = a3
    a5.random = a1

    s = Solution()
    s.copyRandomList(a1)
