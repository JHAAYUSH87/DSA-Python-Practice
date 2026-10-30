# LeetCode 33: Search in Rotated Sorted Array
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([3, 1], 1, 1),
        ([5, 1, 3], 3, 2)
    ]

    for nums, target, expected in test_cases:
        result = solution.search(nums, target)

        print(
            f"Input: nums={nums}, target={target} "
            f"| Output: {result} | Passed: {result == expected}"
        )