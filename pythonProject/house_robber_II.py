from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_util(nums: List[int]) -> int:
            size = len(nums)
            dp = [0] * size

            dp[0] = nums[0]

            if size >= 2:
                dp[1] = max(dp[0], nums[1])

            for i in range(2, size):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

            return dp[-1]

        size = len(nums)
        if size == 1:
            return nums[0]

        if size == 2:
            return max(nums[0], nums[1])

        return max(rob_util(nums[0:size - 1]), rob_util(nums[1:size]))


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 4, 3]
    # nums = [2, 9, 8, 3, 6]
    print(solution.rob(nums))
