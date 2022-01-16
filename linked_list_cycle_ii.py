from common.listnode import ListNode


class Solution():
    """
    Assume the distance from head to the start of the loop is x1
    the distance from the start of the loop to the point fast and slow meet is x2
    the distance from the point fast and slow meet to the start of the loop is x3
    What is the distance fast moved? What is the distance slow moved? And their relationship?

    Fast:               x1 + x2 + x3 + x2
    Slow:               x1 + x2
    Fast == Slow * 2:   x1 + x2 + x3 + x2 = 2 (x1 + x2)
                        Thus x1 = x3
    """
    def getIntersect(self, head):
        tortoise = head
        hare = head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise

        return None

    def detectCycle(self, head):
        if head is None:
            return None

        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1

if __name__ == '__main__':
    s = Solution()
    a1 = ListNode(1)
    print(s.detectCycle(a1))