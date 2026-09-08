#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    char substr[25];
    int* results;
    int size;
} CacheEntry;

CacheEntry memo[500];
int memo_size = 0;

int findInCache(const char* s, int* out_size, int** out_results) {
    for (int i = 0; i < memo_size; i++) {
        if (strcmp(memo[i].substr, s) == 0) {
            *out_size = memo[i].size;
            *out_results = memo[i].results;
            return 1;
        }
    }
    return 0;
}

void addToCache(const char* s, int* results, int size) {
    strcpy(memo[memo_size].substr, s);
    memo[memo_size].results = (int*)malloc(sizeof(int) * size);
    memcpy(memo[memo_size].results, results, sizeof(int) * size);
    memo[memo_size].size = size;
    memo_size++;
}

int* computeWays(const char* s, int* returnSize) {
    int len = strlen(s);
    
    int cached_size;
    int* cached_res;
    if (findInCache(s, &cached_size, &cached_res)) {
        *returnSize = cached_size;
        int* res = (int*)malloc(sizeof(int) * cached_size);
        memcpy(res, cached_res, sizeof(int) * cached_size);
        return res;
    }

    int* results = NULL;
    int capacity = 0;
    int count = 0;
    int is_pure_number = 1;

    for (int i = 0; i < len; i++) {
        char c = s[i];
        if (c == '+' || c == '-' || c == '*') {
            is_pure_number = 0;

            char left_sub[25];
            strncpy(left_sub, s, i);
            left_sub[i] = '\0';
            int left_size;
            int* left_res = computeWays(left_sub, &left_size);

            char right_sub[25];
            strcpy(right_sub, s + i + 1);
            int right_size;
            int* right_res = computeWays(right_sub, &right_size);

            for (int l = 0; l < left_size; l++) {
                for (int r = 0; r < right_size; r++) {
                    if (count >= capacity) {
                        capacity = capacity == 0 ? 16 : capacity * 2;
                        results = (int*)realloc(results, sizeof(int) * capacity);
                    }
                    if (c == '+') results[count++] = left_res[l] + right_res[r];
                    else if (c == '-') results[count++] = left_res[l] - right_res[r];
                    else if (c == '*') results[count++] = left_res[l] * right_res[r];
                }
            }
            free(left_res);
            free(right_res);
        }
    }

    if (is_pure_number) {
        results = (int*)malloc(sizeof(int));
        results[0] = atoi(s);
        count = 1;
    }

    addToCache(s, results, count);
    *returnSize = count;
    return results;
}

int* diffWaysToCompute(char* expression, int* returnSize) {
    for (int i = 0; i < memo_size; i++) {
        free(memo[i].results);
    }
    memo_size = 0;

    return computeWays(expression, returnSize);
}
