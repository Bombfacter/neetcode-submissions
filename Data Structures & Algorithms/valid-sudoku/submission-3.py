class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}


        cols = {}
        boxes = {}

        for row in range(len(board)):
            for col in range(len(board[row])):
                value = board[row][col]

                if value == ".":
                    continue

                box = (row // 3, col // 3)

                if row not in rows:
                    rows[row] = set()

                if col not in cols:
                    cols[col] = set()

                if box not in boxes:
                    boxes[box] = set()

                if value in rows[row]:
                    return False

                if value in cols[col]:
                    return False

                if value in boxes[box]:
                    return False

                rows[row].add(value)
                cols[col].add(value)
                boxes[box].add(value)

        return True
