#include <stdbool.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

bool predictTheWinner(int* nums, int numsSize) {
    if (numsSize <= 1) {
        return true;
    }

    int dp[20][20];

    for (int i = 0; i < numsSize; i++) {
        dp[i][i] = nums[i];
    }

    for (int len = 2; len <= numsSize; len++) {
        for (int i = 0; i <= numsSize - len; i++) {
            int j = i + len - 1;
            dp[i][j] = MAX(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
        }
    }

    return dp[0][numsSize - 1] >= 0;
}
