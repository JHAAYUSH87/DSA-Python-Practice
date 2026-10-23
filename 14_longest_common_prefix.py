
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # fl
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # ""
print(sol.longestCommonPrefix(["apple", "app", "application"]))  # app
