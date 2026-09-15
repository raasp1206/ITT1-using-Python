#include <stdbool.h>

bool canJump(int* nums, int numsSize) {
    int max_reachable = 0;

    for (int i = 0; i < numsSize; i++) {
        if (i > max_reachable) {
            return false;
        }

        if (i + nums[i] > max_reachable) {
            max_reachable = i + nums[i];
        }

        if (max_reachable >= numsSize - 1) {
            return true;
        }
    }

    return max_reachable >= numsSize - 1;
}
