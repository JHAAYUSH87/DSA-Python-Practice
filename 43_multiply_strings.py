
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        result = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                total = product + result[i + j + 1]

                result[i + j + 1] = total % 10
                result[i + j] += total // 10

        return ''.join(map(str, result)).lstrip('0')


# Test Cases
solution = Solution()

tests = [
    ("2", "3", "6"),
    ("123", "456", "56088"),
    ("0", "52", "0"),
    ("99", "99", "9801"),
    ("1234", "5678", "7006652"),
    ("1", "999", "999"),
    ("999", "999", "998001"),
]

for num1, num2, expected in tests:
    result = solution.multiply(num1, num2)
    print(
        f"Input: {num1} x {num2} | Output: {result} | "
        f"Expected: {expected} | Passed: {result == expected}"
    )
