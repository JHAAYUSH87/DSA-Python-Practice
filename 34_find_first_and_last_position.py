# LeetCode 34: Find First and Last Position of Element in Sorted Array
# Time Complexity: O(log n)
# Auxiliary Space: O(1)

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def binary_search(find_first):
            left = 0
            right = len(nums) - 1
            position = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    position = mid

                    if find_first:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return position

        first = binary_search(True)
        last = binary_search(False)

        return [first, last]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([2, 2], 2, [0, 1]),
        ([1, 2, 3, 3, 3, 4], 3, [2, 4])
    ]

    for nums, target, expected in test_cases:
        result = solution.searchRange(nums, target)

        print(
            f"Input: nums={nums}, target={target} | "
            f"Output: {result} | Passed: {result == expected}"
        )