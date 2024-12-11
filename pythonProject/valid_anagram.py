class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s and not t:
            return False

        if t and not s:
            return False

        if len(t) != len(s):
            return False

        first = [0] * 26
        second = [0] * 26

        for i in range(len(s)):
            first[ord(s[i]) - ord('a')] += 1
            second[ord(t[i]) - ord('a')] += 1

        for i in range(0, 26):
            if first[i] != second[i]:
                return False

        return True


if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    solution = Solution()
    print(solution.isAnagram(s, t))
