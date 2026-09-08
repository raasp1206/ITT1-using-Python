#include <stdio.h>
#include <stdlib.h>

char* getPermutation(int n, int k) {
    int fact[10];
    fact[0] = 1;
    for (int i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * i;
    }

    int numbers[9];
    for (int i = 0; i < n; i++) {
        numbers[i] = i + 1;
    }

    char* result = (char*)malloc(sizeof(char) * (n + 1));
    result[n] = '\0';

    k--;

    for (int i = 0; i < n; i++) {
        int block_size = fact[n - 1 - i];
        int index = k / block_size;
        
        result[i] = numbers[index] + '0';

        for (int j = index; j < n - 1 - i; j++) {
            numbers[j] = numbers[j + 1];
        }

        k %= block_size;
    }

    return result;
}
