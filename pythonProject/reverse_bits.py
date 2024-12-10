class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_num, count = 0, 0

        while n:
            bit = n & 1
            reverse_num = reverse_num << 1 | bit
            n = n // 2
            count += 1

        while count < 32:
            reverse_num = reverse_num << 1
            count += 1

        return reverse_num

if __name__ == "__main__":
    solution = Solution()
    n = 21
    print(solution.reverseBits(n))
