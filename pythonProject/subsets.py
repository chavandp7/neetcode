from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for n in nums:
            length = len(result)

            for i in range(length):
                curr_subset = result[i]
                new_subset = curr_subset.copy()
                new_subset.append(n)
                result.append(new_subset)

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets(nums))
