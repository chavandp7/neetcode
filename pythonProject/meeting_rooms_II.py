"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
from typing import List

from interval import Interval


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        nums = set()
        map = defaultdict(list)

        if len(intervals) == 0:
            return 0

        max_count, count = 0, 0
        for interval in intervals:
            start = interval.start
            end = interval.end

            map[start].append(1)
            map[end].append(-1)

            nums.add(start)
            nums.add(end)

        nums = sorted(nums)
        for n in nums:
            values = map[n]

            for i in values:
                count += i

            if count > max_count:
                max_count = count

        return max_count


if __name__ == "__main__":
    solution = Solution()
    intervals = []
    intervals.append(Interval(0, 30))
    intervals.append(Interval(5, 10))
    intervals.append(Interval(10, 15))
    print(solution.minMeetingRooms(intervals))
