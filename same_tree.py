from typing import Optional

from common.treenode import TreeNode


class Solution:
    def isSameTreeBfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        time: n
        space: n
        """
        queue = [(p, q)]

        while queue:
            a, b = queue.pop(0)

            if not a and not b:
                continue
            elif not a or not b:
                return False
            elif a.val != b.val:
                return False

            if a and b:
                queue.append((a.left, b.left))
                queue.append((a.right, b.right))

        return True

    def isSameTreeDfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        time: n
        space: n
        """
        stack = [(p, q)]

        while stack:
            a, b = stack.pop()

            if not a and not b:
                continue
            elif not a or not b:
                return False
            elif a.val != b.val:
                return False

            if a and b:
                stack.append((a.left, b.left))
                stack.append((a.right, b.right))

        return True
