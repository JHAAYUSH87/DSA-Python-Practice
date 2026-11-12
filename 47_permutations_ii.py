
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                current.append(nums[i])

                backtrack()

                current.pop()
                used[i] = False

        backtrack()
        return result


# Test Cases
solution = Solution()

tests = [
    ([1, 1, 2], 3),
    ([1, 2, 3], 6),
    ([1, 1, 1], 1),
    ([0, 0, 1], 3),
    ([-1, -1, 2], 3),
]

for nums, expected in tests:
    result = solution.permuteUnique(nums.copy())
    passed = len(result) == expected and len(set(map(tuple, result))) == expected

    print(
        f"Input: {nums} | Output: {result} | "
        f"Expected unique permutations: {expected} | Passed: {passed}"
    )
