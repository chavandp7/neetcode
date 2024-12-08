class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_palindrome(s, i, j, length):
            start = end = 0

            while i >= 0 and j < length and s[i] == s[j]:
                start = i
                end = j
                i = i - 1
                j = j + 1

            return end + 1 - start, s[start: end + 1]

        length = len(s)
        if length == 1:
            return s

        result = s[0]
        result_len = 1
        for i in range(length - 1):
            curr_length, curr = find_palindrome(s, i, i, length)
            if curr_length > result_len:
                result_len = curr_length
                result = curr

            if s[i] == s[i + 1]:
                curr_length, curr = find_palindrome(s, i, i + 1, length)
                if curr_length > result_len:
                    result_len = curr_length
                    result = curr

        return result


if __name__ == "__main__":
    solution = Solution()
    # s = "ababd"
    s = "abbc"
    print(solution.longestPalindrome(s))
