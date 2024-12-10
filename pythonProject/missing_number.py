from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1 and nums[0] != 0:
            return 0

        total = sum(nums)
        expected_total = length * (length + 1) // 2

        return expected_total - total


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.missingNumber(nums))
