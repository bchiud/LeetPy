from collections import defaultdict
from typing import List


class Solution:
    def canFinishBacktracking(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        dbacktracking
        time: e + v^2 => worst case all nodes are in 1 chain line
        space: e + v
        """
        course_dict = defaultdict(list)
        for post, pre in prerequisites:
            course_dict[pre].append(post)

        path = [False] * numCourses
        for course in range(numCourses):
            if self._isCyclicBacktracking(course, course_dict, path):
                return False

        return True

    def _isCyclicBacktracking(self, curr_course, course_dict, path) -> bool:
        if path[curr_course]:
            return True

        path[curr_course] = True

        isCycle = False
        for course in course_dict[curr_course]:
            if self._isCyclicBacktracking(course, course_dict, path):
                isCycle = True
                break

        path[curr_course] = False
        return isCycle

    def canFinishDfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        toplogical sort: postorder dfs
        time: e + v
        space: e + v
        """
        course_dict = defaultdict(list)
        for post, pre in prerequisites:
            course_dict[pre].append(post)

        visited = [False] * numCourses
        path = [False] * numCourses
        for course in range(numCourses):
            if self._isCyclicDfs(course, course_dict, visited, path):
                return False

        return True

    def _isCyclicDfs(self, current_course, course_dict, visited, path) -> bool:
        if visited[current_course]:
            return False
        if path[current_course]:
            return True

        path[current_course] = True

        ans = False
        for child in course_dict[current_course]:
            if self._isCyclicDfs(child, course_dict, visited, path):
                ans = True
                break

        path[current_course] = False

        return ans

    def canFinishKA(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        toplogical sort: kahn's algorithm
        time: e +v^2
        space: e
        """
        adj = defaultdict(list)
        indegrees = [0] * numCourses

        # build adjacency list
        for pair in prerequisites:
            adj[pair[1]].append(pair[0])
            indegrees[pair[0]] += 1

        # find all vertexes with 0 indegrees
        zero_indegrees = []
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                zero_indegrees.append(course)

        # check if it's one big circle
        if not zero_indegrees:
            return False

        # topological sort
        while zero_indegrees:
            curr = zero_indegrees.pop()
            for out_node in adj[curr]:
                indegrees[out_node] -= 1
                if indegrees[out_node] == 0:
                    zero_indegrees.append(out_node)

        for indegree in indegrees:
            if indegree > 0:
                return False

        return True
