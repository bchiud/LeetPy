class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraphDfs(self, node: 'Node') -> 'Node':
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clone = Node(node.val, [])
        self.visited[node] = clone

        for neigh in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neigh))

        return clone

    def cloneGraphBfs(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited = {}
        visited[node] = Node(node.val, [])
        q = [node]

        while q:
            curr = q.pop(0)

            for n in curr.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    q.append(n)
                visited[curr].neighbors.append(visited[n])

        return visited[node]


if __name__ == '__main__':
    s = Solution()
