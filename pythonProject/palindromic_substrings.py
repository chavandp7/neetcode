class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindromes(s, i, j, length):
            ans = 0

            while i >= 0 and j < length and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1

            return ans

        length = len(s)

        if length == 1:
            return 1

        result = 0
        for i in range(length):
            result += count_palindromes(s, i, i, length)

            if i != length - 1 and s[i] == s[i + 1]:
                result += count_palindromes(s, i, i + 1, length)

        return result


if __name__ == "__main__":
    solution = Solution()
    # s = "abc"
    s = "aaa"

    print(solution.countSubstrings(s))
