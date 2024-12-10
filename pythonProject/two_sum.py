from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in map:
                return [map[rem], i]
            else:
                map[nums[i]] = i

        return [-1, -1]
