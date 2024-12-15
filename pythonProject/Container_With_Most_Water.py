from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left, right = 0, len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            result = max(area, result)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:  # both equal
                right -= 1

        return result


if __name__ == "__main__":
    solution = Solution()
    # height = [1, 7, 2, 5, 4, 7, 3, 6]
    height = [1, 2, 1]
    print(solution.maxArea(height))
