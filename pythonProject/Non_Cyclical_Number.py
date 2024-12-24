class Solution:
    def isHappy(self, n: int) -> bool:
        def find_digit_sums(n):
            sum = 0
            while n:
                rem = n % 10
                sum += rem ** 2
                n = n // 10

            return sum

        sums = set()
        while n:
            sum = find_digit_sums(n)
            if sum == 1:
                return True

            if sum in sums:
                return False

            sums.add(sum)
            n = sum

        return False


if __name__ == "__main__":
    solution = Solution()
    # n = 100
    n = 101
    print(solution.isHappy(n))
