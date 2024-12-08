from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # edge  cases
        if amount == 0:
            return 0

        dp = [float('infinity')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[amount] == float('infinity'):
            return -1

        return int(dp[amount])


if __name__ == "__main__":
    solution = Solution()
    # coins = [1, 5, 10]
    # amount = 12
    # coins = [2]
    # amount = 3
    coins = [1]
    amount = 0
    print(solution.coinChange(coins, amount))
