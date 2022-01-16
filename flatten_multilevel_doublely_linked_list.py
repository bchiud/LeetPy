from common.doubly_linked_listnode import Node


class Solution:
    def flatten(self, head: Node) -> Node:
        if head is None:
            return head
        first, last = self.helper(head)
        return first


    def helper(self, head: 'Node') -> ('Node', 'Node'):
        if not head:
            return

        curr = head
        while curr:
            if curr.child:
                pre, post = curr, curr.next
                child_first, child_last = self.helper(curr.child)
                child_last.next = post
                if post:
                    post.prev = child_last

                pre.next = child_first
                child_first.prev = pre

                curr.child = None
                curr = post
            else:
                curr = curr.next

        curr = head
        while curr.next:
            curr = curr.next

        return head, curr

    def cleaner_flatten(self, head: Node) -> Node:
        if not head:
            return

        dummy = Node(None, None, head, None)
        self.cleaner_helper(dummy, head)

        head.prev = None
        return dummy.next

    def cleaner_helper(self, prev: Node, curr: Node) -> Node:
        if not curr:
            return prev

        prev.next = curr
        curr.prev = prev

        post = curr.next
        tail = self.cleaner_helper(curr, curr.child)
        curr.child = None
        return self.cleaner_helper(tail, post)

    def flattenIterative(self, head: 'Node') -> 'Node':
        if not head:
            return head

        dummy = Node(None, None, head, None)
        prev = dummy

        stack = [head]

        while stack:
            curr = stack.pop()

            prev.next, curr.prev = curr, prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        dummy.next.prev = None
        return dummy.next

if __name__ == '__main__':
    s = Solution()

    nodes = {}
    for i in range(12):
        nodes[i] = Node(i + 1)

    nodes[1].next, nodes[2].prev = nodes[2], nodes[1]
    nodes[2].next, nodes[3].prev = nodes[3], nodes[2]
    nodes[3].next, nodes[4].prev = nodes[4], nodes[3]
    nodes[4].next, nodes[5].prev = nodes[5], nodes[4]
    nodes[5].next, nodes[6].prev = nodes[6], nodes[5]
    nodes[3].child = nodes[7]
    nodes[7].next, nodes[8].prev = nodes[8], nodes[7]
    nodes[8].next, nodes[9].prev = nodes[9], nodes[8]
    nodes[9].next, nodes[10].prev = nodes[10], nodes[9]
    nodes[8].child = nodes[11]
    nodes[11].next, nodes[12].prev = nodes[12], nodes[11]

    s.flatten(nodes[1])
