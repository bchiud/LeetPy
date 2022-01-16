from collections import defaultdict
from typing import List

class Solution:
    def findOrderDFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        toplogical sort: dfs
        time: e + v
        space: e + v
        """
        checked = [False] * numCourses
        adj = defaultdict(list)

        # create adjacency list
        for pair in prerequisites:
            adj[pair[1]].append(pair[0])

        order = []
        path = [False] * numCourses
        for vertex in range(numCourses):
            if checked[vertex]:
                continue
            if not self._dfs(vertex, adj, checked, path, order):
                return []

        return order[::-1]

    def _dfs(self, vertex: int, adj: dict, checked: List, path: List, order: List):
        if path[vertex]:
            return False

        if checked[vertex]:
            return True

        path[vertex] = True
        for out_node in adj[vertex]:
            if not self._dfs(out_node, adj, checked, path, order):
                return False

        path[vertex] = False
        checked[vertex] = True
        order.append(vertex)
        return True

    def findOrderKA(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        toplogical sort: kahn's algorithm
        time: e + v
        space: e + v
        """
        adj = defaultdict(list)
        ids = [0] * numCourses

        for pair in prerequisites:
            adj[pair[1]].append(pair[0])
            ids[pair[0]] += 1

        zero_degree_vertexes = [vertex for vertex, indegrees in enumerate(ids) if indegrees == 0]

        order = []
        while zero_degree_vertexes:
            curr = zero_degree_vertexes.pop()
            order.append(curr)

            for out_vertex in adj[curr]:
                ids[out_vertex] -= 1
                if ids[out_vertex] == 0:
                    zero_degree_vertexes.append(out_vertex)

        return order if len(order) == numCourses else []



if __name__ == '__main__':
    s = Solution()
    s.findOrder(2, [[1, 0]]) == [0, 1]
    # s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 2, 1, 3]
    # s.findOrder(1, []) == [0]
