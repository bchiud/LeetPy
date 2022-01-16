class DLinkedNode:
    def __init__(self):
        self.value = 0
        self.prev = None
        self.next = None


class MRUQueueDLinkedList:
    """
    time: n
    space: n
    """

    def __init__(self, n: int):
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next, self.tail.prev = self.tail, self.head

        for i in range(1, n + 1):
            node = DLinkedNode()
            node.value = i
            self._add_node(node)

    """
    time: n
    """

    def fetch(self, k: int) -> int:
        curr = self.head
        for i in range(k):
            curr = curr.next
        self._remove_node(curr)
        self._add_node(curr)
        return curr.value

    """
    time: 1
    """

    def _add_node(self, node):
        node.prev, node.next = self.tail.prev, self.tail

        self.tail.prev.next = node
        self.tail.prev = node

    """
    time: 1
    """

    def _remove_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev


if __name__ == '__main__':
    dll = MRUQueueDLinkedList(8)
    assert dll.fetch(3) == 3
    assert dll.fetch(5) == 6
    assert dll.fetch(2) == 2
    assert dll.fetch(8) == 2

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
