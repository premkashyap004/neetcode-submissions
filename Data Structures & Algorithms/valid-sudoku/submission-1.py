class Solution:
    def isValidSudoku(self, board):
        seen_in_rows = {}
        seen_in_columns = {}
        seen_in_boxes = {}

        for row_index in range(9):
            for column_index in range(9):
                cell_value = board[row_index][column_index]

                if cell_value == ".":
                    continue

                box_row = row_index // 3
                box_column = column_index // 3
                box_identifier = (box_row, box_column)

                if (row_index, cell_value) in seen_in_rows:
                    return False

                if (column_index, cell_value) in seen_in_columns:
                    return False

                if (box_identifier, cell_value) in seen_in_boxes:
                    return False

                seen_in_rows[(row_index, cell_value)] = True
                seen_in_columns[(column_index, cell_value)] = True
                seen_in_boxes[(box_identifier, cell_value)] = True

        return True
