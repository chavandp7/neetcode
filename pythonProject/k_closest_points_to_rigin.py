from heapq import heappush, heappop
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            x, y = point
            distance = sqrt(x ** 2 + y ** 2)
            heappush(max_heap, (-distance, x, y))
            if len(max_heap) > k:
                heappop(max_heap)

        result = []
        while k > 0 and max_heap:
            distance, x, y = heappop(max_heap)
            result.append([x, y])

        return result


if __name__ == "__main__":
    solution = Solution()
    points = [[0, 2], [2, 2]]
    k = 1
    print(solution.kClosest(points, k))
