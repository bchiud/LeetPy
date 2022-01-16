class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        head = self
        while head and other and head.val == other.val:
            head = head.next
            other = other.next
        if not head and not other:
            return True
        return False

    def __str__(self) -> str:
        list = []
        head = self
        while (head):
            list.append(head.val)
            head = head.next
        return list.__str__()
