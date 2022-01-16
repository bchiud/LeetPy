# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from common.treenode import TreeNode


class Solution:
    def inorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        ans = []
        def helper(root: TreeNode, ans):
            if not root:
                return

            helper(root.left, ans)
            ans.append(root.val)
            helper(root.right, ans)

        helper(root)
        return ans

    def inorderTraversalIterative(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        while True:
            # traverse left as far as possible
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return ans

            # process node
            curr = stack.pop()
            ans.append(curr.val)

            # check right subtree
            root = curr.right