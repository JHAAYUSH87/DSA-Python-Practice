class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    break

                current.append(num)

                # i is used instead of i + 1 because repetition is allowed
                backtrack(i, current, remaining - num)

                current.pop()

        backtrack(0, [], target)
        return result