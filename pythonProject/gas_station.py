from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        sum = 0
        nums = [0] * length

        for i in range(length):
            effective = gas[i] - cost[i]
            nums[i] = effective
            sum += effective

        if sum < 0:
            return -1

        sum, index = 0, -1

        for i in range(length):
            n = nums[i]
            sum += n

            if sum < 0:
                sum = 0
                if n >= 0:
                    index = i
                else:
                    index = -1


            else:
                if index == -1:
                    index = i

        return index

if __name__ == "__main__":
    solution = Solution()
    gas = [1, 2, 3, 4]
    cost = [2, 2, 4, 1]
    print(solution.canCompleteCircuit(gas, cost))