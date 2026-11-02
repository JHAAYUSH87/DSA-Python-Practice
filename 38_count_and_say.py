class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            next_result = ""
            i = 0

            while i < len(result):
                count = 1

                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1

                next_result += str(count) + result[i]
                i += 1

            result = next_result

        return result


# Test cases
solution = Solution()

tests = [
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (4, "1211"),
    (5, "111221"),
    (6, "312211"),
]

for n, expected in tests:
    result = solution.countAndSay(n)
    print(f"Input: n={n} | Output: {result} | Passed: {result == expected}")