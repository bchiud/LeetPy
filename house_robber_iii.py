# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node: TreeNode) -> tuple:
            if not node:
                return (0, 0)

            l_rob, l_skip = helper(node.left)
            r_rob, r_skip = helper(node.right)

            return (node.val + l_skip + r_skip, max(l_rob, l_skip) + max(r_rob, r_skip))

        return max(helper(root))