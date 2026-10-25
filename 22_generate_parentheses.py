
# LeetCode 22: Generate Parentheses
# Time Complexity: O(4^n / sqrt(n))
# Auxiliary Space: O(n), excluding output

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result


if __name__ == "__main__":
    solution = Solution()

    for n in [1, 2, 3]:
        result = solution.generateParenthesis(n)
        print(f"n = {n} | Output: {result}")

    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    actual = solution.generateParenthesis(3)

    print("Test passed:", actual == expected)

