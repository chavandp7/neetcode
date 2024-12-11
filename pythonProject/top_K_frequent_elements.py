import heapq
from collections import defaultdict, Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)
        # print(frequency_map)

        min_heap = []
        for key in frequency_map.keys():
            freq = frequency_map[key]
            heapq.heappush(min_heap, (freq, key))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []
        for (freq, num) in min_heap:
            result.append(num)

        return result


if __name__ == "__main__":
    solution = Solution()
    nums, k = [1, 2, 2, 3, 3, 3], 2
    # nums, k = [7, 7], 1
    print(solution.topKFrequent(nums, k))
