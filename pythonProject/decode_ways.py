class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)

        if s[0] == '0':
            return 0

        if length == 1:
            return 1

        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, length):
            count = 0

            if s[i] != '0':
                count += dp[i]

            num = int(s[i - 1:i + 1])
            if 10 <= num <= 26:
                count += dp[i - 1]

            if count == 0:
                return 0

            dp[i + 1] = count

        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    # s = "1012"
    s = "226"
    print(solution.numDecodings(s))
