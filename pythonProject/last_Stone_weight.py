from heapq import heappush, heappop
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        max_heap = []
        for stone in stones:
            heappush(max_heap, -stone)

        x, y = -1, -1
        while max_heap:
            x = -heappop(max_heap)

            if len(max_heap) == 0:
                return x

            y = -heappop(max_heap)
            x = x - y

            if x != 0:
                heappush(max_heap, -x)

        return 0
