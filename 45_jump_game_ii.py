
class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps


# Test Cases
solution = Solution()

tests = [
    ([2, 3, 1, 1, 4], 2),
    ([2, 3, 0, 1, 4], 2),
    ([1, 2], 1),
    ([0], 0),
    ([1, 1, 1, 1], 3),
    ([2, 1], 1),
    ([1, 2, 3], 2),
]

for nums, expected in tests:
    result = solution.jump(nums)
    print(
        f"Input: {nums} | Output: {result} | "
        f"Expected: {expected} | Passed: {result == expected}"
    )
