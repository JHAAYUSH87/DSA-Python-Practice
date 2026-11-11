
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            elif star != -1:
                j = star + 1
                match += 1
                i = match

            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)


# Test Cases
solution = Solution()

tests = [
    ("aa", "a", False),
    ("aa", "*", True),
    ("cb", "?a", False),
    ("adceb", "*a*b", True),
    ("acdcb", "a*c?b", False),
    ("", "*", True),
    ("", "?", False),
    ("abc", "a**c", True),
    ("abc", "abc", True),
    ("abc", "a*d", False),
]

for s, p, expected in tests:
    result = solution.isMatch(s, p)
    print(
        f"s: {s!r} | p: {p!r} | Output: {result} | "
        f"Expected: {expected} | Passed: {result == expected}"
    )
