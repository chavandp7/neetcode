class Solution:
    def isValid(self, s: str) -> bool:
        def is_match(a, b):
            if a == '(' and b == ')':
                return True

            if a == '[' and b == ']':
                return True

            if a == '{' and b == '}':
                return True

            return False

        stack = []
        open_brackets = {'(', '[', '{'}
        close_brackets = {')', ']', '}'}

        for ch in s:
            if ch in open_brackets:
                stack.append(ch)
                continue

            if ch in close_brackets:
                if not stack:
                    return False

                b = stack.pop()
                if not is_match(b, ch):
                    return False

        if len(stack) != 0:
            return False

        return True
