class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)

        dp = [[0] * (len1 + 1) for _ in range(len2 + 1)]

        for i in range(len2):
            for j in range(len1):
                if text2[i] == text1[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], dp[i][j])

        return dp[len2][len1]


if __name__ == "__main__":
    text1, text2 = "abcd", "abcd"
    # text1, text2 = "abcd", "efgh"
    solution = Solution()
    print(solution.longestCommonSubsequence(text1, text2))
