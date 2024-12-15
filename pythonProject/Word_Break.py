from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        wordDict = set(wordDict)

        for i in range(length):
            for j in range(i, -1, -1):
                if dp[j]:
                    word = s[j:i + 1]
                    if word in wordDict:
                        dp[i + 1] = True
                        break

        return dp[length]


if __name__ == "__main__":
    solution = Solution()
    # s, wordDict = "neetcode", ["neet", "code"]
    # s, wordDict = "applepenapple", ["apple", "pen", "ape"]
    s, wordDict = "catsincars", ["cats","cat","sin","in","car"]

    print(solution.wordBreak(s, wordDict))
