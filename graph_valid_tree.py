from collections import defaultdict
from typing import List


class Solution:
    def validTreeDfs(self, n: int, edges: List[List[int]]) -> bool:
        """
        1. check e == n - 1
        2. check graph is fully connected (i.e. all nodes can be visited)
        time: n
        space: n
        """
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = {0}
        stack = [0]

        while stack:
            curr = stack.pop()
            for neighbor in adj[curr]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                stack.append(neighbor)

        return len(seen) == n

    def validTreeBfs(self, n: int, edges: List[List[int]]) -> bool:
        """
        1. check edges == n - 1
        2. check graph is fully connected (i.e. all nodes can be visited)
        time: n
        space: n
        """
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = {0}
        queue = [0]

        while queue:
            curr = queue.pop(0)
            for neighbor in adj[curr]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)

        return len(seen) == n

    def validTreeUF(self, n: int, edges: List[List[int]]) -> bool:
        """
        time: N⋅α(N) => α(N) is the Inverse Ackermann Function
        space: n
        """
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]

        def find(x):
            return x if parent[x] == x else find(parent[x])

        for e in edges:
            x, y = map(find, e)

            if x == y:  # already been unioned before, therefore must be cyclic
                return False
            parent[x] = y

        return True
