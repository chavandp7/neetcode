from operator import index
from typing import List


class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def util(sum, index, trans_list: List[int]):
            if sum == target:
                result.append(trans_list.copy())
                return

            if index >= len(nums) or sum > target:
                return

            n = nums[index]

            # include
            trans_list.append(n)
            util(sum + n, index, trans_list)

            # not include
            trans_list.pop()
            util(sum, index + 1, trans_list)

        trans_list = []
        result = []

        util(0, 0, trans_list)
        return result


if __name__ == "__main__":
    solution = Solution()
    # nums = [2, 5, 6, 9]
    # target = 9
    nums = [8, 7, 4, 3]
    target = 11
    print(solution.combinationSum(nums, target))
