from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def max_k_replacement():
            if len(map) > k + 1:
                return False

            max_frequency, total_elements = 0, 0
            for key in map.keys():
                if map[key] > max_frequency:
                    max_frequency = map[key]
                total_elements += map[key]

            if total_elements - max_frequency > k:
                return False

            return True

        map = defaultdict(int)
        start, result = 0, 0

        for index, ch in enumerate(s):
            map[ch] += 1

            while start < index and not max_k_replacement():
                starting_char = s[start]
                map[starting_char] -= 1
                start += 1

                if map[starting_char] == 0:
                    del map[starting_char]

            if index - start + 1 > result:
                result = index - start + 1

        return result


if __name__ == "__main__":
    solution = Solution()
    s = "XYYX"
    k = 2
    print(solution.characterReplacement(s, k))
