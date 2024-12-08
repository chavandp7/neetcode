from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curr_max = curr_min = 1

        for num in nums:
            if num == 0:
                curr_max = curr_min = 1
                continue

            temp = curr_max
            curr_max = max(curr_max * num, curr_min * num, num)
            curr_min = min(temp * num, curr_min * num, num)

            result = max(result, curr_max)

        return result


if __name__ == "__main__":
    solution = Solution()
    # nums = [1, 2, -3, 4]
    # nums = [-2, -1]
    nums = [-2, 3, -4]

    print(solution.maxProduct(nums))
