from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        graph = defaultdict(list)
        in_degrees = defaultdict(int)
        queue = deque()

        # build graph and find indegrees - O(E)
        for dest, source in prerequisites:
            graph[source].append(dest)
            in_degrees[dest] += 1

        # find nodes with in degree 0 - O(V)
        for node in range(numCourses):
            if node not in in_degrees:
                queue.append(node)

        topological_sorted_order = []
        # O(V+E)
        while queue:
            node = queue.popleft()
            topological_sorted_order.append(node)

            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1

                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(topological_sorted_order) == numCourses:
            return True

        return False


if __name__ == "__main__":
    solution = Solution()
    # numCourses, prerequisites = 2, [[0, 1]]
    # numCourses, prerequisites = 2, [[0, 1], [1, 0]]
    numCourses, prerequisites = 5, [[1, 4], [2, 4], [3, 1], [3, 2]]
    print(solution.canFinish(numCourses, prerequisites))
