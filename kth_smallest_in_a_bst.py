# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from common.treenode import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        time: n
        space: n
        """
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        return inorder(root)[k - 1]

    def kthSmallestFaster(self, root: Optional[TreeNode], k: int) -> int:
        """
        time: h + k
        space: h
        """
        stack = []
        while True:
            # go as left as much as possible
            while root:
                stack.append(root)
                root = root.left

            # count to k-th
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            else:
                # go right if can't go left
                root = root.right