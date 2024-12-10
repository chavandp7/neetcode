from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)

        if length == 1:
            return True

        if nums[0] == 0:
            return False

        max_reachable = 1
        for i in range(length):
            if i <= max_reachable and nums[i] != 0:
                max_reachable = max(max_reachable, i + nums[i])

        if max_reachable >= length - 1:
            return True

        return False
