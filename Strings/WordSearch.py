class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):
            # All characters matched
            if index == len(word):
                return True

            # Out of bounds or character doesn't match
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[index]):
                return False

            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all four directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))

            # Restore the cell
            board[r][c] = temp

            return found

        # Start DFS from every cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
