#include <stdlib.h>
#include <stdbool.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

void backtrack(int* nums, int numsSize, int* current, int currentSize, bool* used,
               int*** result, int* returnSize, int** returnColumnSizes, int* capacity) {
    if (currentSize == numsSize) {
        if (*returnSize >= *capacity) {
            *capacity *= 2;
            *result = realloc(*result, (*capacity) * sizeof(int*));
            *returnColumnSizes = realloc(*returnColumnSizes, (*capacity) * sizeof(int));
        }
        (*result)[*returnSize] = (int*)malloc(numsSize * sizeof(int));
        for (int i = 0; i < numsSize; i++) {
            (*result)[*returnSize][i] = current[i];
        }
        (*returnColumnSizes)[*returnSize] = numsSize;
        (*returnSize)++;
        return;
    }

    for (int i = 0; i < numsSize; i++) {
        if (used[i]) {
            continue;
        }
        if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
            continue;
        }
        used[i] = true;
        current[currentSize] = nums[i];
        backtrack(nums, numsSize, current, currentSize + 1, used, result, returnSize, returnColumnSizes, capacity);
        used[i] = false;
    }
}

int** permuteUnique(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    qsort(nums, numsSize, sizeof(int), compare);

    int capacity = 10;
    int** result = (int**)malloc(capacity * sizeof(int*));
    *returnColumnSizes = (int*)malloc(capacity * sizeof(int));
    *returnSize = 0;

    int* current = (int*)malloc(numsSize * sizeof(int));
    bool* used = (bool*)calloc(numsSize, sizeof(bool));

    backtrack(nums, numsSize, current, 0, used, &result, returnSize, returnColumnSizes, &capacity);

    free(current);
    free(used);

    return result;
}

