
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n and s[i] == " ":
            i += 1

        sign = 1
        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1

        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")
            num = num * 10 + digit
            i += 1

        num *= sign
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        return max(INT_MIN, min(num, INT_MAX))


sol = Solution()
print(sol.myAtoi("42"))             # 42
print(sol.myAtoi("   -42"))          # -42
print(sol.myAtoi("4193 with words")) # 4193
print(sol.myAtoi("words and 987"))   # 0
