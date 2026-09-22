const char* KEYPAD[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

void backtrack(const char* digits, int index, char* current, char** result, int* returnSize) {
    if (digits[index] == '\0') {
        int len = 0;
        while (current[len] != '\0') len++;
        result[*returnSize] = (char*)malloc((len + 1) * sizeof(char));
        for (int i = 0; i <= len; i++) result[*returnSize][i] = current[i];
        (*returnSize)++;
        return;
    }
    int digit = digits[index] - '0';
    const char* letters = KEYPAD[digit];
    for (int i = 0; letters[i] != '\0'; i++) {
        current[index] = letters[i];
        current[index + 1] = '\0';
        backtrack(digits, index + 1, current, result, returnSize);
    }
}

char** letterCombinations(char* digits, int* returnSize) {
    *returnSize = 0;
    int len = 0;
    while (digits[len] != '\0') len++;
    if (len == 0) return NULL;
    int maxCombinations = 1;
    for (int i = 0; i < len; i++) {
        int d = digits[i] - '0';
        int cLen = 0;
        while (KEYPAD[d][cLen] != '\0') cLen++;
        maxCombinations *= cLen;
    }
    char** result = (char**)malloc(maxCombinations * sizeof(char*));
    char* current = (char*)malloc((len + 1) * sizeof(char));
    backtrack(digits, 0, current, result, returnSize);
    free(current);
    return result;
}
