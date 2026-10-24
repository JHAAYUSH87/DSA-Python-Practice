
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return closest


if __name__ == "__main__":
    sol = Solution()

    print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # Expected: 2
    print(sol.threeSumClosest([0, 0, 0], 1))        # Expected: 0
