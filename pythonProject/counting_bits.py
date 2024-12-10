from typing import List


class Solution:

    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        if n == 0:
            return result

        result[1] = 1
        power_of_2 = 1

        for i in range(2, n + 1):
            if i == 2 * power_of_2:
                power_of_2 = 2 * power_of_2

            result[i] = 1 + result[i - power_of_2]

        return result
