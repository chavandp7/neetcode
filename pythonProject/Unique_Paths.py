class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * n for _ in range(m)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    matrix[r][c] = 1
                elif r == m - 1 or c == n - 1:
                    matrix[r][c] = 1
                else:
                    matrix[r][c] += matrix[r][c + 1] + matrix[r + 1][c]

        return matrix[0][0]


if __name__ == "__main__":
    solution = Solution()
    # m, n = 3, 6
    m, n = 3, 3
    print(solution.uniquePaths(m, n))
