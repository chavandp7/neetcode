class Solution():

    def find_next_larger(self, arr: list):
        result = []
        if not arr:
            return result

        length = len(arr)
        result = [0] * length
        stack = []

        result[length - 1] = -1
        stack.append(arr[length - 1])

        for i in range(length - 2, -1, -1):
            n = arr[i]

            while stack and n >= stack[-1]:
                stack.pop()

            if not stack:
                result[i] = -1
            else:
                result[i] = stack[-1]

            stack.append(n)

        return result


if __name__ == "__main__":
    solution = Solution()
    arr = [22, 1, 4, 5, 7, 8, 9, 6, 3, 2, 10, 11, 23]
    print(arr)
    print(solution.find_next_larger(arr))
