from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def unique():
            for key in map.keys():
                if map[key] > 1:
                    return False

            return True

        if not s or len(s) == 0:
            return 0

        map = defaultdict(int)
        result = 0
        start = 0

        for index, ch in enumerate(s):
            map[ch] += 1

            while start < index and not unique():
                start_char = s[start]
                map[start_char] -= 1
                start += 1
                if map[start_char] == 0:
                    del map[start_char]

            if len(map) > result:
                result = len(map)

        return result


if __name__ == "__main__":
    solution = Solution()
    # s = "zxyzxyz"
    s = "xxxx"
    print(solution.lengthOfLongestSubstring(s))
