from collections import defaultdict
from email.policy import default
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1

            new_str = ''
            for i in range(0, 26):
                if freq[i] != 0:
                    new_str += chr(ord('a') + i) + str(freq[i])

            map[new_str].append(s)

        result = []
        for key in map.keys():
            result.append(map[key])

        return result


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(Solution().groupAnagrams(strs))
