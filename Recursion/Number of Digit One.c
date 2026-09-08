int countDigitOne(int n) {
    if (n <= 0) {
        return 0;
    }

    long long count = 0;
    for (long long i = 1; i <= n; i *= 10) {
        long long divider = i * 10;
        
        count += (n / divider) * i;
        
        long long current_digit_val = n % divider;
        if (current_digit_val >= 2 * i) {
            count += i;
        } else if (current_digit_val >= i) {
            count += (current_digit_val - i + 1);
        }
    }

    return (int)count;
}
