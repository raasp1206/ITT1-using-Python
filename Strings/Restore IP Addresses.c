#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Helper to check if a segment is a valid IP integer (0-255, no leading zeros)
bool isValid(const char* s, int start, int len) {
    if (len <= 0 || len > 3) return false;
    if (len > 1 && s[start] == '0') return false; // Leading zero rule
    
    int val = 0;
    for (int i = 0; i < len; i++) {
        val = val * 10 + (s[start + i] - '0');
    }
    return val <= 255;
}

void backtrack(const char* s, int sLen, int start, int segment, char* current, int curLen, char** result, int* returnSize) {
    if (segment == 4) {
        if (start == sLen) {
            result[*returnSize] = (char*)malloc((curLen) * sizeof(char));
            for (int i = 0; i < curLen - 1; i++) {
                result[*returnSize][i] = current[i];
            }
            result[*returnSize][curLen - 1] = '\0';
            (*returnSize)++;
        }
        return;
    }
    int remChars = sLen - start;
    int remSegments = 4 - segment;
    if (remChars < remSegments || remChars > remSegments * 3) return;
    for (int len = 1; len <= 3 && start + len <= sLen; len++) {
        if (isValid(s, start, len)) {
            for (int i = 0; i < len; i++) {
                current[curLen + i] = s[start + i];
            }
            current[curLen + len] = '.'; 
            
            backtrack(s, sLen, start + len, segment + 1, current, curLen + len + 1, result, returnSize);
        }
    }
}


char** restoreIpAddresses(char* s, int* returnSize) {
    *returnSize = 0;
    int sLen = strlen(s);
    
    if (sLen < 4 || sLen > 12) {
        return NULL;
    }
    
    char** result = (char**)malloc(100 * sizeof(char*));
    

    char current[16]; 
    
    backtrack(s, sLen, 0, 0, current, 0, result, returnSize);
    
    return result;
}
