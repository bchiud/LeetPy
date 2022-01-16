"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = deque([(root, 0)])
        while queue:
            curr, level = queue.popleft()

            if len(ans) <= level:
                ans.append([])
            ans[level].append(curr.val)

            for c in curr.children:
                queue.append((c, level + 1))

        return ans