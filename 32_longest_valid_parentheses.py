# LeetCode 32: Longest Valid Parentheses
# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        ("()()", 4),
        ("((()))", 6),
        ("(((((", 0),
        ("()(()", 2)
    ]

    for s, expected in test_cases:
        result = solution.longestValidParentheses(s)

        print(
            f"Input: s='{s}' | Output: {result} "
            f"| Passed: {result == expected}"
        )