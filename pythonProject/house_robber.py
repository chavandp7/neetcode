from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0] * size

        dp[0] = nums[0]
        if size >= 2:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, size):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


if __name__ == "__main__":
    nums = [1, 1, 3, 3]
    # nums = [2, 9, 8, 3, 6]
    solution = Solution()
    print(solution.rob(nums))
