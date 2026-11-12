
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()


# Test Cases
solution = Solution()

tests = [
    (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    ),
    (
        [[5, 1, 9, 11], [2, 4, 8, 10],
         [13, 3, 6, 7], [15, 14, 12, 16]],
        [[15, 13, 2, 5], [14, 3, 4, 1],
         [12, 6, 8, 9], [16, 7, 10, 11]]
    ),
    ([[1]], [[1]]),
    ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
]

for matrix, expected in tests:
    solution.rotate(matrix)
    print(
        f"Output: {matrix} | Expected: {expected} | "
        f"Passed: {matrix == expected}"
    )
