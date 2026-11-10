
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


# Test Cases
solution = Solution()

tests = [
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1),
    ([1, 2, 3], 4),
    ([1, 1], 2),
    ([], 1),
    ([2], 1),
    ([2, 1], 3),
    ([-1, -2], 1),
]

for nums, expected in tests:
    result = solution.firstMissingPositive(nums.copy())
    print(
        f"Input: {nums} | Output: {result} | "
        f"Expected: {expected} | Passed: {result == expected}"
    )
