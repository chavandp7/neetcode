from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index, inserted = -1, False
        stack = []

        for i, interval in enumerate(intervals):
            start, end = interval
            if start <= newInterval[0] <= end:
                index = i + 1
                break
            elif newInterval[0] < start:
                index = i
                break

        if index == -1:
            intervals.append(newInterval)
        else:
            intervals.insert(index, newInterval)

        for i in range(len(intervals) - 1, -1, -1):
            stack.append(intervals[i])

        result = []
        while len(stack) >= 2:
            interval1 = stack.pop()
            interval2 = stack.pop()

            if interval1[0] <= interval2[0] <= interval1[1]:
                new_interval = [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
                stack.append(new_interval)
            else:
                result.append(interval1)
                stack.append(interval2)

        while stack:
            result.append(stack.pop())

        return result


if __name__ == "__main__":
    solution = Solution()
    # intervals, newInterval = [[1, 2], [3, 5], [9, 10]], [6, 7]
    intervals, newInterval = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    print(solution.insert(intervals, newInterval))
