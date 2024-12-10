class Solution:
    def getSum(self, a: int, b: int) -> int:
        tmp = 0

        while b != 0:
            tmp = (a & b) << 1
            a = a ^ b
            b = tmp

        return a

