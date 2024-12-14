from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        length = len(nums)

        result = set()
        for i in range(length - 2):
            n = nums[i]

            left = i + 1
            right = length - 1
            while left < right:
                sum = n + nums[left] + nums[right]
                if sum == 0:
                    result.add((n, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        ans = []
        for item in result:
            ans.append(list(item))

        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums))
