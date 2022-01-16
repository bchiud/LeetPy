from typing import List

from common.treenode import TreeNode


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        leaves = []

        def bfs(curr):
            if not curr:
                return -1
            left = bfs(curr.left)
            right = bfs(curr.right)
            level = max(left, right) + 1
            if level >= len(leaves):
                leaves.append([])
            leaves[level].append(curr.val)
            return level

        bfs(root)

        return leaves

if __name__ == '__main__':
    s = Solution()

    ll = TreeNode(4)
    lr = TreeNode(5)
    r = TreeNode(3)
    l = TreeNode(2, ll, lr)
    root = TreeNode(1, l, r)

    print(s.findLeaves(root))