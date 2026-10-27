# LeetCode 28: Find the Index of the First Occurrence in a String
# Time Complexity: O(n * m)
# Space Complexity: O(1)

class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("mississippi", "issip", 4),
        ("abc", "", 0)
    ]

    for haystack, needle, expected in test_cases:
        result = solution.strStr(haystack, needle)
        print(
            f"Input: haystack='{haystack}', needle='{needle}' "
            f"| Output: {result} | Passed: {result == expected}"
        )