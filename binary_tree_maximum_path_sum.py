from common.treenode import TreeNode


class Solution:
    def maxPathSumRecursive(self, root: TreeNode) -> int:
        max_path = float('-inf')

        def dfs(curr):
            nonlocal max_path
            if not curr:
                return 0

            left = max(dfs(curr.left), 0)
            right = max(dfs(curr.right), 0)

            total = left + curr.val + right
            max_path = max(max_path, total)

            return curr.val + max(left, right)

        dfs(root)
        return max_path
