class Solution:
    def isValidSudoku(self, board):
        seen_in_rows = []
        seen_in_cols = []
        seen_in_boxes = []

        for row in range(9):
            for col in range(9):
                cell_value = board[row][col]
                if cell_value == ".":
                    continue

                if (row, cell_value) in seen_in_rows:
                    return False
                
                if (col, cell_value) in seen_in_cols:
                    return False
                
                box_value = (row // 3, col //3)
                if (box_value, cell_value) in seen_in_boxes:
                    return False
                
                seen_in_rows.append((row, cell_value))
                seen_in_cols.append((col, cell_value))
                seen_in_boxes.append((box_value, cell_value))



        return True
