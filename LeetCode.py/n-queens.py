class Solution(object):
    def solveNQueens(self, n):
        solutions = []
        board = [["."] * n for _ in range(n)]
        
        cols = set()
        pos_diagonals = set()
        neg_diagonals = set()
        
        def backtrack(row):
            if row == n:
                current_board = ["".join(r) for r in board]
                solutions.append(current_board)
                return
            
            for col in range(n):
                if col in cols or (row + col) in pos_diagonals or (row - col) in neg_diagonals:
                    continue
                
                cols.add(col)
                pos_diagonals.add(row + col)
                neg_diagonals.add(row - col)
                board[row][col] = "Q"
                
                backtrack(row + 1)
                
                cols.remove(col)
                pos_diagonals.remove(row + col)
                neg_diagonals.remove(row - col)
                board[row][col] = "."
                
        backtrack(0)
        return solutions
