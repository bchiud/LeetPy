class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        time: 1
        """
        return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        time: 1
        """
        return self.s1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        time: 1
        """
        return not self.s1


class MyQueueFaster:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.newest = []  # newest on top
        self.oldest = []  # oldest on top

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        time: 1
        """
        self.newest.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        time: 1
        """
        self.peek()
        return self.oldest.pop()

    def peek(self) -> int:
        """
        Get the front element.
        time: amortize 1 => oldest is already filled for n - 1 calls
        """
        if not self.oldest:
            while self.newest:
                self.oldest.append(self.newest.pop())
        return self.oldest[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        time: 1
        """
        return not self.newest and not self.oldest

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
