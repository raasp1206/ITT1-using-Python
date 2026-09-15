#include <stdbool.h>

bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    int rows[9] = {0};
    int cols[9] = {0};
    int boxes[9] = {0};

    for (int r = 0; r < 9; r++) {
        for (int c = 0; c < 9; c++) {
            char val = board[r][c];

            if (val == '.') {
                continue;
            }

            int num_shift = val - '1';
            int mask = 1 << num_shift;
            
            int box_index = (r / 3) * 3 + (c / 3);

            if ((rows[r] & mask) || (cols[c] & mask) || (boxes[box_index] & mask)) {
                return false; 
            }

            rows[r] |= mask;
            cols[c] |= mask;
            boxes[box_index] |= mask;
        }
    }

    return true;
}
