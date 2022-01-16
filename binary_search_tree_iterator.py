# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from common.treenode import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        """
        time: h => n if all nodes are left childs
        space: h => n if all nodes are left childs
        """
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        """
        time: 1 (amortized since each node is only visited once)
        space: 1
        """
        ans = self.stack.pop()

        curr = ans.right
        while curr:
            self.stack.append(curr)
            curr = curr.left

        return ans.val


    def hasNext(self) -> bool:
        """
        time: 1
        space: 1
        """
        return self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()