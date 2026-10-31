class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


# Test cases
solution = Solution()

tests = [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([], 3, 0),
]

for nums, target, expected in tests:
    result = solution.searchInsert(nums, target)
    print(
        f"Input: nums={nums}, target={target} | "
        f"Output: {result} | Passed: {result == expected}"
    )