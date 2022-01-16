# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from common.treenode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node: TreeNode, floor: int, ceil: int):
            if not node:
                return True

            if node.val <= floor or ceil <= node.val:
                return False

            return helper(node.left, floor, node.val) and helper(node.right, node.val, ceil)

        return helper(root, float('-inf'), float('inf'))