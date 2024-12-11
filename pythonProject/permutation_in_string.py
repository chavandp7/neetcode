from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def is_permutation():
            if len(c1) != len(c2):
                return False

            for key in c1.keys():
                if key not in c2 or c1[key] != c2[key]:
                    return False

            return True

        if (s1 and not s2) or (s2 and not s1) or (len(s1) > len(s2)):
            return False

        c1 = Counter(s1)
        length1 = len(s1)
        c2 = Counter(s2[0:length1 - 1])
        start = 0

        for index in range(length1 - 1, len(s2)):
            ch = s2[index]
            if ch in c2:
                c2[ch] += 1
            else:
                c2[ch] = 1

            if is_permutation():
                return True

            starting_char = s2[start]
            c2[starting_char] -= 1

            if c2[starting_char] == 0:
                del c2[starting_char]

            start += 1

        return False


if __name__ == "__main__":
    solution = Solution()
    s1, s2 = "abc", "lecabee"
    print(solution.checkInclusion(s1, s2))
