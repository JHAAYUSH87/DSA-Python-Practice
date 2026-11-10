
class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water


# Test Cases
solution = Solution()

tests = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([1, 0, 1], 1),
    ([3, 0, 2, 0, 4], 7),
    ([1, 2, 3, 4], 0),
    ([5, 4, 3, 2, 1], 0),
    ([], 0),
]

for height, expected in tests:
    result = solution.trap(height)
    print(
        f"Input: {height} | Output: {result} | "
        f"Expected: {expected} | Passed: {result == expected}"
    )
