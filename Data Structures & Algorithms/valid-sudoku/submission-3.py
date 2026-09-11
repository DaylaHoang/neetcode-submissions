# Plan
        # 1. create 9 sets for rows, columns, boxes
        # 2. scan every cell
        # 3. skip "."
        # 4. calculate the box index
        # 5. If the digit already exists in any of the 3 sets -> return False
                # add the digit to all three sets
        # If we finishing scanning, True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                digit = board[row][col]

                box_index = (row // 3) * 3 + (col // 3)

                if (
                    digit in rows[row]
                    or digit in cols[col]
                    or digit in boxes[box_index]
                ):
                    return False
                rows[row].add(digit)
                cols[col].add(digit)
                boxes[box_index].add(digit)
        return True
    
