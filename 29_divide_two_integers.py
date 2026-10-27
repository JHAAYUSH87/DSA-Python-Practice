# LeetCode 29: Divide Two Integers
# Time Complexity: O(log^2 n)
# Space Complexity: O(1)

class Solution:
    def divide(self, dividend, divisor):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Handle 32-bit integer overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Double divisor using bit shifting
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (10, 3, 3),
        (7, -3, -2),
        (0, 1, 0),
        (1, 1, 1),
        (-10, 3, -3),
        (-10, -3, 3),
        (10, -3, -3),
        (2**31 - 1, 1, 2**31 - 1),
        (-2**31, -1, 2**31 - 1),
        (-2**31, 1, -2**31)
    ]

    for dividend, divisor, expected in test_cases:
        result = solution.divide(dividend, divisor)

        print(
            f"Input: dividend={dividend}, divisor={divisor} "
            f"| Output: {result} | Passed: {result == expected}"
        )