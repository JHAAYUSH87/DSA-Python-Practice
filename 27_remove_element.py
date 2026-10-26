
# LeetCode 27: Remove Element
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
        ([1], 1, []),
        ([1, 2, 3], 4, [1, 2, 3]),
        ([], 0, [])
    ]

    for nums, val, expected in test_cases:
        k = solution.removeElement(nums, val)
        actual = nums[:k]

        print(
            f"Input: {nums}, val={val} | "
            f"Result: {actual} | Passed: {sorted(actual) == sorted(expected)}"
        )
