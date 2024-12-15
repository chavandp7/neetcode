from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            result.append(word)
            i = j + 1 + length

        return result

if __name__ == "__main__":
    solution = Solution()
    strs = ["neet","code","love","you"]
    print(strs)
    s = solution.encode(strs)
    print(s)
    print(solution.decode(s))
