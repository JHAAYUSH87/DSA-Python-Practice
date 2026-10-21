
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        max_length = 1

        for i in range(len(s)):
            for left, right in [(i, i), (i, i + 1)]:
                while (
                    left >= 0
                    and right < len(s)
                    and s[left] == s[right]
                ):
                    if right - left + 1 > max_length:
                        start = left
                        max_length = right - left + 1

                    left -= 1
                    right += 1

        return s[start:start + max_length]
sol = Solution()

print(sol.longestPalindrome("babad"))  # Expected: bab or aba
print(sol.longestPalindrome("cbbd"))   # Expected: bb