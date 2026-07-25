class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row has any zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column has any zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero the first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero the first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
