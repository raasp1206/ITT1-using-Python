int lastRemaining(int n) {
    int head = 1;     
    int step = 1;      
    int remaining = n; 
    int left = 1;      
    while (remaining > 1) {

        if (left || (remaining % 2 == 1)) {
            head += step;
        }

        remaining /= 2;
        step *= 2;
        left = !left;
    }

    return head;
}
