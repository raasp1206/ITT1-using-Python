#include <stdbool.h>

bool isMatch(char* s, char* p) {
    int s_ptr = 0, p_ptr = 0;
    int s_star = -1, p_star = -1;

    while (s[s_ptr] != '\0') {
        if (p[p_ptr] == s[s_ptr] || p[p_ptr] == '?') {
            s_ptr++;
            p_ptr++;
        }
        else if (p[p_ptr] == '*') {
            p_star = p_ptr;
            s_star = s_ptr;
            p_ptr++;
        }
        else if (p_star != -1) {
            p_ptr = p_star + 1; 
            s_star++;           
            s_ptr = s_star;     
        }
        else {
            return false;
        }
    }

    while (p[p_ptr] == '*') {
        p_ptr++;
    }

    return p[p_ptr] == '\0';
}
