
# LeetCode 26: Remove Duplicates from Sorted Array
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
        ([1], [1]),
        ([], [])
    ]

    for nums, expected in test_cases:
        k = solution.removeDuplicates(nums)
        actual = nums[:k]

        print(
            f"Input result: {actual} | Count: {k} "
            f"| Passed: {actual == expected}"
        )
