from collections import OrderedDict


class LRUCacheOrderedDict(OrderedDict):

    """
    space: n
    """
    def __init__(self, capacity: int):
        self.capcity = capacity

    """
    time: 1
    """
    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    """
    time: 1
    """
    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capcity:
            self.popitem(last=False)


class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCacheDLinkedList:
    """
    space: 1
    """
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next, self.tail.prev = self.tail, self.head

    """
    time: 1
    """
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    """
    time: 1
    """
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node:
            node = DLinkedNode()
            node.key = key
            node.value = value
            self.cache[key] = node
            self._add_node(node)
            self.size += 1

            if self.size > self.capacity:
                last: DLinkedNode = self._pop_tail()
                del self.cache[last.key]
                self.size -= 1

        else:
            node.value = value
            self._move_to_head(node)

    def _add_node(self, node: DLinkedNode) -> None:
        node.prev, node.next = self.head, self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node: DLinkedNode):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DLinkedNode:
        last = self.tail.prev
        self._remove_node(last)
        return last

    def _remove_node(self, node: DLinkedNode) -> None:
        node.prev.next, node.next.prev = node.next, node.prev


if __name__ == '__main__':
    od = LRUCacheOrderedDict(2)
    od.put(1, 1)
    od.put(2, 2)
    assert od.get(2) == 2
    od.put(3, 3)
    assert od.get(1) == -1

    dll = LRUCacheDLinkedList(2)
    od.put(1, 1)
    od.put(2, 2)
    assert od.get(2) == 2
    od.put(3, 3)
    assert od.get(1) == -1
