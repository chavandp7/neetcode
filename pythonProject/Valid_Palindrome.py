class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        s = s.lower()
        start, end = 0, len(s) - 1

        while start < end:
            ch_left = s[start]
            if not ch_left.isalnum():
                start += 1
                continue

            ch_right = s[end]
            if not ch_right.isalnum():
                end -= 1
                continue

            if ch_left != ch_right:
                return False

            start += 1
            end -= 1

        return True

