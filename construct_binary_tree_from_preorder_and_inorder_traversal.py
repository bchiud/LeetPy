# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from common.treenode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preorder_index = 0

        inorder_value_to_index = {}
        for i, v in enumerate(inorder):
            inorder_value_to_index[v] = i

        def helper(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            cur_val = preorder[preorder_index]
            root = TreeNode(cur_val)

            preorder_index += 1

            root.left = helper(left, inorder_value_to_index[cur_val] - 1)
            root.right = helper(inorder_value_to_index[cur_val] + 1, right)

            return root

        return helper(0, len(inorder) - 1)