from math import sqrt


class Solution():

    def find_min_numbers(self, n: int):
        if n <= 3:
            return n

        dp = [float('infinity')] * (n + 1)

        for i in range(4):
            dp[i] = i

        for i in range(4, n + 1):
            square_root = int(sqrt(i))

            if square_root * square_root == i:
                dp[i] = 1
                continue

            for j in range(1, square_root + 1):
                square_j = j * j
                dp[i] = min(dp[i], 1 + dp[i - square_j])

        return dp[n]

if __name__ == "__main__":
    solution = Solution()
    n = 32
    print(solution.find_min_numbers(n))
