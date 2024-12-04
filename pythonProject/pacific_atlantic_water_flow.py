from collections import deque
from typing import List


class Solution:
    def valid(self, x, y, rows, cols):
        if x < 0 or x >= rows:
            return False

        if y < 0 or y >= cols:
            return False

        return True

    def bfs(self, queue, rows, cols, heights):
        reachable = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            reachable.add((r, c))

            for (x, y) in directions:
                dx, dy = r + x, c + y

                if not self.valid(dx, dy, rows, cols):
                    continue

                if (dx, dy) in reachable:
                    continue

                if heights[dx][dy] < heights[r][c]:
                    continue

                queue.append((dx, dy))

        return reachable

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        if rows == 0 or cols == 0:
            return []

        pacific = deque()
        atlantic = deque()

        for i in range(rows):
            pacific.append((i, 0))
            atlantic.append((i, cols - 1))

        for i in range(cols):
            pacific.append((0, i))
            atlantic.append((rows - 1, i))

        pacific = self.bfs(pacific, rows, cols, heights)
        atlantic = self.bfs(atlantic, rows, cols, heights)
        result = []

        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])

        return result


if __name__ == "__main__":
    solution = Solution()
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(solution.pacificAtlantic(heights))
