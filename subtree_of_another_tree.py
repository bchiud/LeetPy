# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

from common.treenode import TreeNode


class Solution:
    def isSubtreeDFS(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        time: n * m
        space: n * m
        """
        if not root:
            return False
        if self.compareTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtreeBFSLevel(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        q = deque([root])
        while q:
            curr = q.popleft()

            if self.compareTree(curr, subRoot):
                return True

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return False

    def compareTree(self, a: TreeNode, b: TreeNode):
        # if a and b:
        #     return a.val == b.val and self.compareTree(a.left, b.left) and self.compareTree(a.right, b.right)
        # return False

        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return self.compareTree(a.left, b.left) and self.compareTree(a.right, b.right)