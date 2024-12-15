from collections import defaultdict
from typing import List


class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != parent:
                    result = dfs(neighbor, node)
                    if not result:
                        return False

            return True

        if len(edges) > n - 1:
            return False

        visited = set()
        graph = defaultdict(list)

        for edge in edges:
            x, y = edge
            graph[x].append(y)
            graph[y].append(x)

        result = dfs(0, 0)
        if not result:
            return False

        if len(visited) != n:
            return False

        return True
