from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length

        dp[0] = 1
        for i in range(1, length):
            n = nums[i]
            count = 0

            for j in range(i):
                if n > nums[j]:
                    count = max(dp[j], count)

            dp[i] = count + 1

        return max(dp)


if __name__ == "__main__":
    solution = Solution()
    # nums = [9, 1, 4, 2, 3, 3, 7]
    nums = [0, 3, 1, 3, 2, 3]
    print(solution.lengthOfLIS(nums))
