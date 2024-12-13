from collections import defaultdict
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            last_item = result[-1]

            if intervals[i][0] <= last_item[1]:
                last_item[1] = max(last_item[1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result


if __name__ == "__main__":
    solution = Solution()
    # intervals = [[1, 3], [1, 5], [6, 7]]
    # intervals = [[1, 2], [2, 3]]
    intervals = [[1, 4], [0, 0]]

    print(solution.merge(intervals))
