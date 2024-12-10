from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0

        max_reachable, min_jumps = 0, 0

        for i in range(length):
            if max_reachable >= i and nums[i] != 0:
                temp = max(max_reachable, i + nums[i])
                if temp > max_reachable:
                    max_reachable = temp
                    min_jumps += 1

                if max_reachable >= length - 1:
                    return min_jumps

        return min_jumps
