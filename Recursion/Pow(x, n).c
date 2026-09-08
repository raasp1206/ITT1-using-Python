double myPow(double x, int n) {
    // Base case: any number raised to the power of 0 is 1
    if (n == 0) {
        return 1.0;
    }
    
    // Store 'n' in a long long to safely handle overflow 
    // when negating INT_MIN (-2147483648)
    long long N = n;
    
    // If the exponent is negative, invert the base and make the exponent positive
    if (N < 0) {
        x = 1.0 / x;
        N = -N;
    }
    
    double result = 1.0;
    double current_product = x;
    
    // Binary exponentiation loop
    while (N > 0) {
        // If the current exponent bit is odd, multiply the result by current product
        if (N % 2 == 1) {
            result *= current_product;
        }
        // Square the base product
        current_product *= current_product;
        // Divide the exponent by 2
        N /= 2;
    }
    
    return result;
}
