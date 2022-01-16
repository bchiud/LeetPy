from collections import defaultdict
from typing import List


class Solution:
    def countComponentsBfs(self, n: int, edges: List[List[int]]) -> int:
        """
        time: e + v
        space: e + v
        """
        adj = defaultdict(list)
        for pair in edges:  # 2e space
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])

        visited = [False] * n  # v space
        components = 0
        for i in range(n):
            if not visited[i]:
                components += 1
                visited[i] = True
                q = [i]  # worst case is v space
                while q:
                    cur = q.pop(0)
                    for j in adj[cur]:
                        if not visited[j]:
                            visited[j] = True
                            q.append(j)

        return components

    def countComponentsDfs(self, n: int, edges: List[List[int]]) -> int:
        """
        time: e + v
        space: e + v
        """
        adj = defaultdict(list)
        for pair in edges:  # 2e space
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])

        visited = [False] * n
        def dfs(i):
            for j in adj[i]:
                if not visited[j]:
                    visited[j] = True
                    dfs(j)

        components = 0
        for i in range(n):
            if not visited[i]:
                components += 1
                visited[i] = True
                dfs(i)

        return components

    def countComponentsUF(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        def find(v):
            # traverse until found parent
            if p[v] != v:
                p[v] = find(p[v])
            return p[v]
        for e in edges:
            v, w = map(find, e)  # search parent for both edges in pair
            p[v] = w  # union
            n -= v != w  # reduce component count if not already same parent
        return n

if __name__ == '__main__':
    s = Solution()
    assert s.countComponentsBfs(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert s.countComponentsDfs(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert s.countComponentsUF(5, [[0, 1], [1, 2], [3, 4]]) == 2
