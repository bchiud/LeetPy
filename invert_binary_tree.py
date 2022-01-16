# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from common.treenode import TreeNode


class Solution:
    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root

    def invertTreeBfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        q = [root]

        while q:
            curr = q.pop(0)
            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return root

    def invertTreeDfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        stack = [root]

        while stack:
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return root