# Assume I am having an array of interger elemenets and total have 50,000 elements in array. Write a code to find the duplicates in array


class Solution():
    def find_duplicates(self, arr):
        result = []
        occureence = set()

        if not arr:
            return result

        for index, element in enumerate(arr):
            if element in occureence:
                result.append([index, element])
            else:
                occureence.add(element)

        return result

    def find_longest_palindrome(self, s):
        def find_indexes_of_palindrome(start_index, end_index):
            while start_index >= 0 and end_index < length and s[start_index] == s[end_index]:
                start_index -= 1
                end_index += 1

            return start_index + 1, end_index - 1

        start, end = 0, 0
        max_length = 0
        length = len(s)
        if not s:
            return None

        for i, ch in enumerate(s):
            start_index, end_index = find_indexes_of_palindrome(i - 1, i + 1)
            if end_index - start_index + 1 > max_length:
                max_length = end_index - start_index + 1
                start = start_index
                end = end_index

            if i < length - 1 and s[i] == s[i + 1]:
                start_index, end_index = find_indexes_of_palindrome(i - 1, i + 2)
                if end_index - start_index + 1 > max_length:
                    max_length = end_index - start_index + 1
                    start = start_index
                    end = end_index

        return s[start: end + 1]


if __name__ == "__main__":
    # arr = [2, 4, 5, 7, 4, 8, 2, 7]
    solution = Solution()
    # print(solution.find_duplicates(arr))

    s = "forgeeksskeegfor"
    print(solution.find_longest_palindrome(s))
