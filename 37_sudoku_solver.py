class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num != ".":
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        box = (r // 3) * 3 + (c // 3)

                        for num in "123456789":
                            if (
                                num not in rows[r]
                                and num not in cols[c]
                                and num not in boxes[box]
                            ):
                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[box].add(num)

                                if backtrack():
                                    return True

                                board[r][c] = "."
                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[box].remove(num)

                        return False

            return True

        backtrack()


# Test case
solution = Solution()

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solution.solveSudoku(board)

print("Solved Sudoku:")
for row in board:
    print(row)