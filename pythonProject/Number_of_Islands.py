from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if (r, c) in visited:
                return

            visited.add((r, c))
            if grid[r][c] == "0":
                return

            for dx, dy in directions:
                x = r + dx
                y = c + dy

                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                    dfs(x, y)

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    result += 1
                    dfs(r, c)

        return result


if __name__ == "__main__":
    solution = Solution()
    # grid = [
    #     ["0", "1", "1", "1", "0"],
    #     ["0", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]

    grid = [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(solution.numIslands(grid))
