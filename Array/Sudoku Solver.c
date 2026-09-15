#include <stdbool.h>

int rows[9];
int cols[9];
int boxes[9];
bool backtrack(char** board, int r, int c) {
    if (c == 9) {
        r++;
        c = 0;
    }
    
    if (r == 9) {
        return true;
    }

    if (board[r][c] != '.') {
        return backtrack(board, r, c + 1);
    }

    int box_index = (r / 3) * 3 + (c / 3);

    for (char digit = '1'; digit <= '9'; digit++) {
        int num_shift = digit - '1';
        int mask = 1 << num_shift;

        if (!(rows[r] & mask) && !(cols[c] & mask) && !(boxes[box_index] & mask)) {
            board[r][c] = digit;
            rows[r] |= mask;
            cols[c] |= mask;
            boxes[box_index] |= mask;
            if (backtrack(board, r, c + 1)) {
                return true;
            }

            board[r][c] = '.';
            rows[r] &= ~mask;
            cols[c] &= ~mask;
            boxes[box_index] &= ~mask;
        }
    }

    return false; 
}
void solveSudoku(char** board, int boardSize, int* boardColSize) {
    for (int i = 0; i < 9; i++) {
        rows[i] = 0;
        cols[i] = 0;
        boxes[i] = 0;
    }

    for (int r = 0; r < 9; r++) {
        for (int c = 0; c < 9; c++) {
            if (board[r][c] != '.') {
                int num_shift = board[r][c] - '1';
                int mask = 1 << num_shift;
                int box_index = (r / 3) * 3 + (c / 3);
                
                rows[r] |= mask;
                cols[c] |= mask;
                boxes[box_index] |= mask;
            }
        }
    }

    backtrack(board, 0, 0);
}
