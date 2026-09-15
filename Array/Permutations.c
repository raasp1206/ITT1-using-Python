#include <stdlib.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void backtrack(int* nums, int numsSize, int start, int*** result, int* returnSize) {

    if (start == numsSize) {
        (*result)[*returnSize] = (int*)malloc(numsSize * sizeof(int));
        for (int i = 0; i < numsSize; i++) {
            (*result)[*returnSize][i] = nums[i];
        }
        (*returnSize)++;
        return;
    }

    for (int i = start; i < numsSize; i++) {
        swap(&nums[start], &nums[i]);       
        backtrack(nums, numsSize, start + 1, result, returnSize); /
        swap(&nums[start], &nums[i]);      
    }
}

int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int total_permutations = 1;
    for (int i = 1; i <= numsSize; i++) {
        total_permutations *= i;
    }
    int** result = (int**)malloc(total_permutations * sizeof(int*));
    *returnColumnSizes = (int*)malloc(total_permutations * sizeof(int));
    *returnSize = 0;

    backtrack(nums, numsSize, 0, &result, returnSize);

    for (int i = 0; i < total_permutations; i++) {
        (*returnColumnSizes)[i] = numsSize;
    }

    return result;
}
