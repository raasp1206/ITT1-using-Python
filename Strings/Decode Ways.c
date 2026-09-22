#include <string.h>

int numDecodings(char* s) {
    if (s == NULL || s[0] == '0') {
        return 0;
    }
    
    int len = strlen(s);
    if (len == 1) {
        return 1;
    }
    
    // dp1 represents ways to decode string ending at index i-1
    // dp2 represents ways to decode string ending at index i-2
    int dp2 = 1; 
    int dp1 = 1; 
    int current = 0;
    
    for (int i = 1; i < len; i++) {
        current = 0;
        
        // Check single-digit decoding for s[i]
        if (s[i] != '0') {
            current += dp1;
        }
        
        // Check two-digit decoding for s[i-1] and s[i]
        int twoDigit = (s[i - 1] - '0') * 10 + (s[i] - '0');
        if (twoDigit >= 10 && twoDigit <= 26) {
            current += dp2;
        }
        
        // If it's impossible to decode up to this character, break early
        if (current == 0) {
            return 0;
        }
        
        // Shift state variables forward
        dp2 = dp1;
        dp1 = current;
    }
    
    return dp1;
}
