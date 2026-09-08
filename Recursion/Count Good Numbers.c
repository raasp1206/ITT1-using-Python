#include <stdio.h>

long long power(long long base, long long exp) {
    long long res = 1;
    long long MOD = 1000000007;
    base = base % MOD;
    
    while (exp > 0) {
        if (exp % 2 == 1) {
            res = (res * base) % MOD;
        }
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int countGoodNumbers(long long n) {
    long long MOD = 1000000007;
    
    long long even_indices = (n + 1) / 2;
    long long odd_indices = n / 2;
    
    long long even_choices = power(5, even_indices);
    long long odd_choices = power(4, odd_indices);
    
    return (int)((even_choices * odd_choices) % MOD);
}
