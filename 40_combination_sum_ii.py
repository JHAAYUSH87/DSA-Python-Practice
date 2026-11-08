class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):

                # Skip duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                current.append(candidates[i])

                backtrack(i + 1, current, remaining - candidates[i])

                current.pop()

        backtrack(0, [], target)
        return result


# Test cases
solution = Solution()

tests = [
    ([10, 1, 2, 7, 6, 1, 5], 8,
     [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),

    ([2, 5, 2, 1, 2], 5,
     [[1, 2, 2], [5]]),

    ([2], 1, []),

    ([1, 1, 1, 1, 1], 2,
     [[1, 1]]),
]

for candidates, target, expected in tests:
    result = solution.combinationSum2(candidates, target)
    passed = sorted(result) == sorted(expected)

    print(
        f"Input: candidates={candidates}, target={target}"
        f" | Output: {result} | Passed: {passed}"
    )