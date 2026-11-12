
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        current = []

        def backtrack():
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack()
                    current.pop()

        backtrack()
        return result


# Test Cases
solution = Solution()

tests = [
    ([1, 2, 3], 6),
    ([0, 1], 2),
    ([1], 1),
    ([1, 2], 2),
    ([-1, 0, 1], 6),
]

for nums, expected in tests:
    result = solution.permute(nums)
    passed = len(result) == expected and len(set(map(tuple, result))) == expected

    print(
        f"Input: {nums} | Output: {result} | "
        f"Expected permutations: {expected} | Passed: {passed}"
    )
