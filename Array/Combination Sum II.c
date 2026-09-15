#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

void backtrack(int* candidates, int candidatesSize, int target, int start, 
               int* current, int currentSize, int*** result, int* returnSize, int** returnColumnSizes) {
    
    if (target == 0) {
        *result = realloc(*result, (*returnSize + 1) * sizeof(int*));
        *returnColumnSizes = realloc(*returnColumnSizes, (*returnSize + 1) * sizeof(int));
        
        (*result)[*returnSize] = (int*)malloc(currentSize * sizeof(int));
        for (int i = 0; i < currentSize; i++) {
            (*result)[*returnSize][i] = current[i];
        }
        
        (*returnColumnSizes)[*returnSize] = currentSize;
        (*returnSize)++;
        return;
    }

    for (int i = start; i < candidatesSize; i++) {

        if (candidates[i] > target) {
            break;
        }

        if (i > start && candidates[i] == candidates[i - 1]) {
            continue;
        }

        current[currentSize] = candidates[i];
        
        backtrack(candidates, candidatesSize, target - candidates[i], i + 1, 
                  current, currentSize + 1, result, returnSize, returnColumnSizes);
    }
}

int** combinationSum2(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {
    qsort(candidates, candidatesSize, sizeof(int), compare);

    *returnSize = 0;
    int** result = NULL;
    *returnColumnSizes = NULL;
    
    int* current = (int*)malloc(candidatesSize * sizeof(int));

    backtrack(candidates, candidatesSize, target, 0, current, 0, &result, returnSize, returnColumnSizes);
    free(current);

    return result;
}
